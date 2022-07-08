#!/usr/bin/env python3

import datetime

from backend_api.api_views.classes.models import Class_Student
from backend_api.api_views.attendance.models import LongTermAbsence

from .report import Report


class AttendanceSheet(Report):

    def __init__(self, lesson):
        self.lesson = lesson
        self.header_text = f"Attendance: {self.lesson.class_fk.name} {self.lesson.start_datetime:%Y.%m.%d %H:%M}"
        super().__init__()

    def populate(self):

        self.add_heading("Class details", 1),
        self.add_key_value_pair(
            "Subject", self.lesson.subject_level.subject.name),
        self.add_key_value_pair("Level", self.lesson.subject_level.name)

        # get the students that belong in this class
        cls = self.lesson.class_fk
        students = Class_Student.objects.filter(
            class_fk=cls).order_by("student__last_name")
        students = [cs.student for cs in students]

        # get any ongoing long-term absences
        today = datetime.date.today()
        ltas = []
        absent = set()
        for student in students:
            ltas += [*LongTermAbsence.objects.filter(
                student=student, start_date__lte=today, end_date__gte=today)]

        if ltas:
            self.add_heading(f"Ongoing long-term absences", 1)
        for lta in ltas:
            student = lta.student
            absent.add(student)

            dates_reason = f"{lta.start_date:%Y.%m.%d}--{lta.end_date:%Y.%m.%d} ({lta.reason})"
            self.add_key_value_pair(
                f"{student.first_name} {student.last_name}", dates_reason)

        # add a row for each student
        self.add_heading("Attendance", 1)
        student_names = []
        for student in students:
            name = f"{student.last_name.upper()}, {student.first_name}"
            if student in absent:
                name += " (LTA)"
            student_names += [name]
        self.add_attendance_table(student_names)
