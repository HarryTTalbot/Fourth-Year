from django.urls import reverse

from datetime import datetime, timedelta, timezone

from backend_api.tests.api_test_case import APITestCase

from backend_api.api_views.attendance.models import *


class LessonViewSetTestCase(APITestCase):

    def test_today(self):
        now = datetime.now(tz=timezone.utc)
        Lesson.objects.create(
            start_datetime=now, end_datetime=now+timedelta(hours=1), class_fk=self.class1, subject_level=self.subject_level1
        )
        response = self.client.get(
            reverse('lesson-today'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_get_attendance(self):
        response = self.client.get(
            reverse('lesson-get-attendance', kwargs={'pk': self.lesson1.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['status'], 'P')

        response = self.client.get(
            reverse('lesson-get-attendance', kwargs={'pk': self.lesson2.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['status'], 'A')

        response = self.client.get(
            reverse('lesson-get-attendance', kwargs={'pk': self.lesson3.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['status'], '')

    def test_set_attendance(self):
        response = self.client.post(
            reverse('lesson-set-attendance', kwargs={'pk': self.lesson1.pk}), data=[{'student': self.student2.id, 'status': 'P'}], content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(Attendance.objects.filter(lesson=self.lesson1)), 2)
        self.assertEqual(len(Attendance.objects.filter(
            lesson=self.lesson1, student=self.student2, status='P')), 1)

        response = self.client.post(
            reverse('lesson-set-attendance', kwargs={'pk': self.lesson2.pk}), data=[{'student': self.student1.id, 'status': 'P'}], content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(Attendance.objects.filter(lesson=self.lesson2)), 1)
        self.assertEqual(len(Attendance.objects.filter(
            lesson=self.lesson1, student=self.student1, status='P')), 1)
