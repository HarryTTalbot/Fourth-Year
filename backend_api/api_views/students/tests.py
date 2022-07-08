from django.urls import reverse

from backend_api.tests.api_test_case import APITestCase

from backend_api.api_views.students.models import *


class StudentViewSetTestCase(APITestCase):

    def test_get_classes(self):
        response = self.client.get(
            reverse('student-get-classes', kwargs={'pk': self.student1.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], self.class1.id)

    def test_get_contacts(self):
        response = self.client.get(
            reverse('student-get-contacts', kwargs={'pk': self.student1.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(
            response.data[0]['contact_id']['id'], self.contact1.id)

    def test_add_contacts(self):
        response = self.client.post(
            reverse('student-add-contacts', kwargs={'pk': self.student1.pk}), data=[{'contact_id': self.contact2.id, 'relationship': 'testR'}], content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Student_Contact.objects.all()), 2)
        self.assertEqual(len(Student_Contact.objects.filter(student_id=self.student1,
                                                            contact_id=self.contact2)), 1)

        invalidData = [
            [{'contact_id': self.contact2.id, 'relationship': 'testR'}],
            [{'contact_id': -1, 'relationship': 'testR'}],
            [{'contact_id': self.contact2.id}],
            [{'contact_id': 'a', 'relationship': 'testR'}],
            [{'contact_id': self.contact2.id, 'relationship': 1}],
            [{'invalid': self.contact2.id}],
        ]

        for data in invalidData:
            response = self.client.post(
                reverse('student-add-contacts', kwargs={'pk': self.student1.pk}), data=data, content_type='application/json')
            self.assertEqual(response.status_code, 400)

    def test_remove_contacts(self):
        response = self.client.post(
            reverse('student-remove-contacts', kwargs={'pk': self.student1.pk}), data=[{'contact_id': self.contact1.id}], content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Student_Contact.objects.all()), 0)

        invalidData = [
            [{'contact_id': self.contact1.id}],
            [{'contact_id': self.contact1.id}],
            [{'contact_id': self.contact1.id}],
            [{'contact_id': 'a'}],
            [{'invalid': self.contact2.id}],
        ]

        for data in invalidData:
            response = self.client.post(
                reverse('student-add-contacts', kwargs={'pk': self.student1.pk}), data=data, content_type='application/json')
            self.assertEqual(response.status_code, 400)

    def test_get_lessons(self):
        response = self.client.get(
            reverse('student-get-lessons', kwargs={'pk': self.student1.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(
            response.data[0]['id'], self.lesson1.id)
        self.assertEqual(response.data[0]['subject']['id'], self.subject1.id)

    def test_get_attendance(self):
        response = self.client.get(
            reverse('student-get-attendance', kwargs={'pk': self.student1.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(
            response.data[0]['status'], 'P')
        self.assertEqual(
            response.data[0]['lesson']['id'], self.lesson1.id)
        self.assertEqual(
            response.data[1]['status'], '')
        self.assertEqual(
            response.data[1]['lesson']['id'], self.lesson2.id)
        self.assertEqual(
            response.data[2]['status'], '')
        self.assertEqual(
            response.data[2]['lesson']['id'], self.lesson3.id)


class ContactsViewSetTestCase(APITestCase):

    def test_get_students(self):
        response = self.client.get(
            reverse('contact_detail-get-students', kwargs={'pk': self.contact1.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['relationship'], 'test-r')
        self.assertEqual(
            response.data[0]['student_id']['id'], self.student1.id)
