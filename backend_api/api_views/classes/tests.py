from django.urls import reverse

from backend_api.tests.api_test_case import APITestCase

from backend_api.api_views.classes.models import *


class ClassViewSetTestCase(APITestCase):

    def test_get_students(self):
        response = self.client.get(
            reverse('class-get-students', kwargs={'pk': self.class1.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], self.student1.id)

        response = self.client.get(
            reverse('class-get-students', kwargs={'pk': self.class2.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_students_not_in_class(self):
        response = self.client.get(
            reverse('class-get-students-not-in-class', kwargs={'pk': self.class1.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], self.student2.id)

        response = self.client.get(
            reverse('class-get-students-not-in-class', kwargs={'pk': self.class2.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_add_students(self):
        response = self.client.post(
            reverse('class-add-students', kwargs={'pk': self.class1.pk}), data=[{'student_id': self.student2.id}], content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Class_Student.objects.all()), 2)
        self.assertEqual(len(Class_Student.objects.filter(class_fk=self.class1,
                                                          student=self.student2)), 1)

        invalidData = [
            [{'student_id': 3}],
            [{'student_id': 'a'}],
            [{'invalid': 2}],
        ]

        for data in invalidData:
            response = self.client.post(
                reverse('class-add-students', kwargs={'pk': self.class1.pk}), data=data, content_type='application/json')
            self.assertEqual(response.status_code, 400)

    def test_remove_students(self):
        response = self.client.post(
            reverse('class-remove-students', kwargs={'pk': self.class1.pk}), data=[{'student_id': 1}], content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Class_Student.objects.all()), 0)

        invalidData = [
            [{'student_id': 3}],
            [{'student_id': 'a'}],
            [{'invalid': 2}],
        ]

        for data in invalidData:
            response = self.client.post(
                reverse('class-remove-students', kwargs={'pk': self.class1.pk}), data=data, content_type='application/json')
            self.assertEqual(response.status_code, 400)

    def test_set_students(self):
        response = self.client.post(
            reverse('class-set-students', kwargs={'pk': self.class1.pk}), data=[{'student_id': 2}], content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Class_Student.objects.all()), 1)
        self.assertEqual(len(Class_Student.objects.filter(class_fk=self.class1,
                                                          student=self.student2)), 1)

        invalidData = [
            [{'student_id': 3}],
            [{'student_id': 'a'}],
            [{'invalid': 2}],
        ]

        for data in invalidData:
            response = self.client.post(
                reverse('class-remove-students', kwargs={'pk': self.class1.pk}), data=data, content_type='application/json')
            self.assertEqual(response.status_code, 400)
