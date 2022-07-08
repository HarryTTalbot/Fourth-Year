from django.urls import reverse

from backend_api.tests.api_test_case import APITestCase

from backend_api.api_views.inventory.models import *


class BulkItemViewSet(APITestCase):
    def test_withdraw(self):
        response = self.client.post(
            reverse('bulkitem-withdraw',
                    kwargs={'pk': self.bulk_item.pk}),
            data={'staff_id': self.staff.id, 'quantity': 5},
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.bulk_item.refresh_from_db()
        self.assertEqual(self.bulk_item.quantity, 5)
        self.assertEqual(len(BulkItemLog.objects.all()), 3)

        invalidData = [
            {'staff_id': -1, 'quantity': 5},
            {'staff_id': 'a', 'quantity': 5},
            {'quantity': 5},
            {'staff_id': self.staff.id, 'quantity': 10},
            {'staff_id': self.staff.id, 'quantity': 0},
            {'staff_id': self.staff.id, 'quantity': -5},
        ]

        for data in invalidData:
            response = self.client.post(
                reverse('bulkitem-withdraw',
                        kwargs={'pk': self.bulk_item.pk}),
                data=data,
                content_type='application/json')
            self.assertEqual(response.status_code, 400)

    def test_restock(self):
        response = self.client.post(
            reverse('bulkitem-restock',
                    kwargs={'pk': self.bulk_item.pk}),
            data={'staff_id': self.staff.id, 'quantity': 5},
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.bulk_item.refresh_from_db()
        self.assertEqual(self.bulk_item.quantity, 15)
        self.assertEqual(len(BulkItemLog.objects.all()), 3)

        invalidData = [
            {'staff_id': -1, 'quantity': 5},
            {'staff_id': 'a', 'quantity': 5},
            {'quantity': 5},
            {'staff_id': self.staff.id, 'quantity': 0},
            {'staff_id': self.staff.id, 'quantity': -5},
        ]

        for data in invalidData:
            response = self.client.post(
                reverse('bulkitem-withdraw',
                        kwargs={'pk': self.bulk_item.pk}),
                data=data,
                content_type='application/json')
            self.assertEqual(response.status_code, 400)

    def test_history(self):
        response = self.client.get(
            reverse('bulkitem-history', kwargs={'pk': self.bulk_item.pk}))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['type'], 'R')
        self.assertEqual(response.data[1]['type'], 'W')


class WorksheetViewSet(APITestCase):
    def test_withdraw(self):
        response = self.client.post(
            reverse('worksheet-withdraw',
                    kwargs={'pk': self.worksheet.pk}),
            data={'staff_id': self.staff.id, 'quantity': 5},
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.worksheet.refresh_from_db()
        self.assertEqual(self.worksheet.quantity, 5)
        self.assertEqual(len(WorksheetLog.objects.all()), 3)

        invalidData = [
            {'staff_id': -1, 'quantity': 5},
            {'staff_id': 'a', 'quantity': 5},
            {'quantity': 5},
            {'staff_id': self.staff.id, 'quantity': 10},
            {'staff_id': self.staff.id, 'quantity': 0},
            {'staff_id': self.staff.id, 'quantity': -5},
        ]

        for data in invalidData:
            response = self.client.post(
                reverse('worksheet-withdraw',
                        kwargs={'pk': self.worksheet.pk}),
                data=data,
                content_type='application/json')
            self.assertEqual(response.status_code, 400)

    def test_restock(self):
        response = self.client.post(
            reverse('worksheet-restock',
                    kwargs={'pk': self.worksheet.pk}),
            data={'staff_id': self.staff.id, 'quantity': 5},
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.worksheet.refresh_from_db()
        self.assertEqual(self.worksheet.quantity, 15)
        self.assertEqual(len(WorksheetLog.objects.all()), 3)

        invalidData = [
            {'staff_id': -1, 'quantity': 5},
            {'staff_id': 'a', 'quantity': 5},
            {'quantity': 5},
            {'staff_id': self.staff.id, 'quantity': 0},
            {'staff_id': self.staff.id, 'quantity': -5},
        ]

        for data in invalidData:
            response = self.client.post(
                reverse('worksheet-withdraw',
                        kwargs={'pk': self.worksheet.pk}),
                data=data,
                content_type='application/json')
            self.assertEqual(response.status_code, 400)

    def test_history(self):
        response = self.client.get(
            reverse('worksheet-history', kwargs={'pk': self.worksheet.pk}))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['type'], 'R')
        self.assertEqual(response.data[1]['type'], 'W')


class ItemLoanViewSet(APITestCase):
    def test_create(self):
        response = self.client.post(
            reverse('itemloan-list'),
            data={'item_id': self.lendable_item1.id,
                  'student_id': self.student1.id, 'quantity': 5},
            content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.lendable_item1.refresh_from_db()
        self.assertEqual(self.lendable_item1.quantity_available, 5)
        self.assertEqual(len(ItemLoan.objects.all()), 3)

        invalidData = [
            {'student_id': -1, 'quantity': 5},
            {'student_id': 'a', 'quantity': 5},
            {'quantity': 5},
            {'student_id': self.staff.id, 'quantity': 10},
            {'student_id': self.staff.id, 'quantity': 0},
            {'student_id': self.staff.id, 'quantity': -5},
        ]

        for data in invalidData:
            response = self.client.post(
                reverse('itemloan-list'),
                data=data,
                content_type='application/json')
            self.assertEqual(response.status_code, 400)

    def test_update(self):
        response = self.client.patch(
            reverse('itemloan-detail', kwargs={'pk': self.item_loan1.pk}),
            data={'quantity': 6},
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.lendable_item1.refresh_from_db()
        self.assertEqual(self.lendable_item1.quantity_available, 9)
        self.assertEqual(len(ItemLoan.objects.all()), 2)

        response = self.client.patch(
            reverse('itemloan-detail', kwargs={'pk': self.item_loan1.pk}),
            data={'item_id': 2, 'quantity': 7},
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.lendable_item1.refresh_from_db()
        self.lendable_item2.refresh_from_db()
        self.assertEqual(self.lendable_item1.quantity_available, 15)
        self.assertEqual(self.lendable_item2.quantity_available, 3)
        self.assertEqual(len(ItemLoan.objects.all()), 2)

        response = self.client.patch(
            reverse('itemloan-detail', kwargs={'pk': self.item_loan1.pk}),
            data={'item_id': 1},
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.lendable_item1.refresh_from_db()
        self.lendable_item2.refresh_from_db()
        self.assertEqual(self.lendable_item1.quantity_available, 8)
        self.assertEqual(self.lendable_item2.quantity_available, 10)
        self.assertEqual(len(ItemLoan.objects.all()), 2)

        invalidData = [
            {'student_id': -1, 'quantity': 5},
            {'student_id': 'a', 'quantity': 5},
            {'quantity': 5},
            {'student_id': self.staff.id, 'quantity': 10},
            {'student_id': self.staff.id, 'quantity': 0},
            {'student_id': self.staff.id, 'quantity': -5},
        ]

        for data in invalidData:
            response = self.client.post(
                reverse('itemloan-list'),
                data=data,
                content_type='application/json')
            self.assertEqual(response.status_code, 400)

    def test_destroy(self):
        response = self.client.delete(
            reverse('itemloan-detail', kwargs={'pk': self.item_loan1.pk}))
        self.assertEqual(response.status_code, 204)
        self.lendable_item1.refresh_from_db()
        self.assertEqual(self.lendable_item1.quantity_available, 15)
        self.assertEqual(len(ItemLoan.objects.all()), 1)

    def test_return_item(self):
        response = self.client.post(
            reverse('itemloan-return-item', kwargs={'pk': self.item_loan1.pk}),
            data={'quantity': 3},
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.lendable_item1.refresh_from_db()
        self.assertEqual(self.lendable_item1.quantity_available, 13)
        self.assertEqual(len(ItemLoan.objects.all()), 1)
        self.assertEqual(len(ItemLoanLog.objects.all()), 3)

        invalidData = [
            {'quantity': 11},
            {'quantity': -1}
        ]

        for data in invalidData:
            response = self.client.post(
                reverse('itemloan-return-item',
                        kwargs={'pk': self.item_loan2.pk}),
                data=data,
                content_type='application/json')
            self.assertEqual(response.status_code, 400)

    def test_history(self):
        response = self.client.get(
            reverse('itemloan-history'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['quantity_returned'], 0)
        self.assertEqual(response.data[1]['quantity_returned'], 5)
