from django.urls import reverse

from backend_api.tests.api_test_case import APITestCase

from backend_api.api_views.subjects.models import *


class SubjectViewSetTestCase(APITestCase):

    def test_get_levels(self):
        response = self.client.get(
            reverse('subject-get-levels', kwargs={'pk': self.subject1.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], self.subject_level1.id)

    def test_add_level(self):
        response = self.client.post(
            reverse('subject-add-level', kwargs={'pk': self.subject1.pk}), data={'name': 'testS1L2'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(Subject_Level.objects.filter(subject=self.subject1)), 2)
        self.assertEqual(
            len(Subject_Level.objects.filter(subject=self.subject2)), 1)

    def test_remove_level(self):
        response = self.client.post(
            reverse('subject-remove-level', kwargs={'pk': self.subject1.pk}), data={'id': self.subject_level1.id}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(Subject_Level.objects.filter(subject=self.subject1)), 0)
        self.assertEqual(
            len(Subject_Level.objects.filter(subject=self.subject2)), 1)
