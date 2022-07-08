#!/usr/bin/env python3

import datetime

from backend_api.api_views.centre_details.models import CenterDetails
from backend_api.api_views.attendance.models import ATTENDANCE_TYPES, Attendance, Lesson, LongTermAbsence
from backend_api.api_views.classes.models import Class_Student
from backend_api.api_views.students.models import Student_Contact
from backend_api.api_views.inventory.models import ItemLoan, ItemLoanLog

from .report import Report


class StudentDataReport(Report):
    "Contains all data stored about a particular student"

    def __init__(self, student):
        self.student = student

        name = f"{self.student.last_name.upper()}, {self.student.first_name}"
        if self.student.middle_name:
            name += " " + self.student.middle_name
        self.header_text = f"Student Data Report: {name}"

        super().__init__()

    def populate(self):
        # store the student's personal details and address
        self.add_heading("Personal details", 1)
        self.add_key_value_pair("Forename", self.student.first_name)
        self.add_key_value_pair("Middle name(s)", self.student.middle_name),
        self.add_key_value_pair("Surname", self.student.last_name),
        self.add_key_value_pair("Date of birth", self.student.date_of_birth),
        self.add_key_value_pair("Date joined", self.student.join_date),
        self.add_key_value_pair("Date left", self.student.leave_date),
        self.add_key_value_pair("Telephone number", self.student.phone_number),
        self.add_key_value_pair("School", self.student.school),
        self.add_key_value_pair("Grade", self.student.grade),
        self.add_key_value_pair("Email address", self.student.email)

        self.add_heading("Address", 2),
        self.add_key_value_pair("Line one", self.student.address.line_one),
        self.add_key_value_pair("Line two", self.student.address.line_two),
        self.add_key_value_pair("Line three", self.student.address.line_three),
        self.add_key_value_pair("City/Town", self.student.address.city_town),
        self.add_key_value_pair("Province/District",
                                self.student.address.province_district),
        self.add_key_value_pair("Post code", self.student.address.post_code),
        self.add_key_value_pair("Country", self.student.address.country)

        # store the personal details and addresses of every contact associated with
        # the student
        student_contacts = Student_Contact.objects.filter(
            student_id=self.student.id)
        for i, student_contact in enumerate(student_contacts):
            contact = student_contact.contact_id

            # :p
            key = {
                0: "Primary contact",
                1: "Secondary contact",
                2: "Tertiary contact",
            }.get(i, f"Additional contact (#{i+1})")

            self.add_heading(key, 1),
            self.add_key_value_pair("Forename", contact.first_name),
            self.add_key_value_pair("Middle name(s)", contact.middle_name),
            self.add_key_value_pair("Surname", contact.last_name),
            self.add_key_value_pair(
                "Home telephone number", contact.phone_home),
            self.add_key_value_pair(
                "Work telephone number", contact.phone_business),
            self.add_key_value_pair(
                "Mobile telephone number", contact.phone_mobile),
            self.add_key_value_pair("Email address", contact.email),
            self.add_key_value_pair(
                "Relationship", student_contact.relationship)

            self.add_heading("Address", 2),
            self.add_key_value_pair("Line one", contact.address.line_one),
            self.add_key_value_pair("Line two", contact.address.line_two),
            self.add_key_value_pair("Line three", contact.address.line_three),
            self.add_key_value_pair("City/Town", contact.address.city_town),
            self.add_key_value_pair(
                "Province/District", contact.address.province_district),
            self.add_key_value_pair("Post code", contact.address.post_code),
            self.add_key_value_pair("Country", contact.address.country)

        # store information about every class that a student has been associated with
        # there is a size-1 heading for each class, and a size-2 heading for each
        # combination of class, subject, and level. Each class-subject-level heading
        # contains all of the attendance recorded for that combination
        classes = Class_Student.objects.filter(student=self.student.id)
        for cls in classes:
            cls = cls.class_fk
            self.add_heading(f"Class \"{cls.name}\"", 1)

            # get a list of all subject-level combinations for this class
            subject_levels = set()
            lessons = Lesson.objects.filter(class_fk=cls.id)
            for lesson in lessons:
                # only record subject-levels where this student attended one of the
                # lessons
                if Attendance.objects.filter(student=self.student.id, lesson=lesson.id).exists():
                    subject_levels.add(lesson.subject_level)
            # at this point, if cls is "Mr Lock's class" and subject_levels contains
            # "advanced Albanian language", it means that "advanced Albanian language"
            # was taught in "Mr Lock's class"; by the design of the database, the
            # student we are looking was registered for the class

            # iterate over the subject-levels we have collected...
            for subject_level in subject_levels:
                self.add_heading(
                    f"{subject_level.subject.name} ({subject_level.name})", 2)
                # find the lessons for this subject level where attendance was recorded
                # for this student and sort by lesson start time
                attendances = Attendance.objects.filter(
                    student=self.student.id, lesson__subject_level=subject_level.id).order_by("lesson__start_datetime")
                for attendance in attendances:
                    lesson = attendance.lesson

                    # each individual attendance record is its own key-value pair. If
                    # the lesson start date and end date are different, then we want
                    # to show both in the key, otherwise we show only the start date
                    if lesson.start_datetime.date() == lesson.end_datetime.date():
                        key = f"{lesson.start_datetime:%Y.%m.%d %H:%M}--{lesson.end_datetime:%H:%M}"
                    else:
                        key = f"{lesson.start_datetime:%Y.%m.%d %H:%M}--{lesson.end_datetime:%Y.%m.%d %H:%M}"

                    # the value for the key-value pair is the student's status
                    # TODO Django docs suggest that attendance.status.label should work
                    # but it doesn't
                    status = dict(ATTENDANCE_TYPES)[attendance.status]
                    self.add_key_value_pair(key, status)

        # record information about long-term absences
        self.add_heading("Long-term absences", 1)
        ltas = LongTermAbsence.objects.filter(student=self.student.id)
        for i, lta in enumerate(ltas):
            self.add_heading(f"Long-term absence #{i+1}", 2)
            self.add_key_value_pair("Start date", lta.start_date),
            self.add_key_value_pair("End date", lta.end_date),
            self.add_key_value_pair("Reason", lta.reason)

        self.add_heading("Inventory logs", 1)
        self.add_heading("Current loans", 2)
        loans = ItemLoan.objects.filter(student_id=self.student)
        for loan in loans:
            self.add_key_value_pair(
                f"{loan.created_at:%Y.%m.%d %H:%M}", f"{loan.quantity} of {loan.item_id.name}")

        self.add_heading("Past loans", 2)
        loans = ItemLoanLog.objects.filter(student_id=self.student)
        for loan in loans:
            self.add_key_value_pair(f"{loan.loan_datetime:%Y.%m.%d %H:%M}--{loan.created_at:%Y.%m.%d %H:%M}",
                                    f"{loan.quantity_lent} (returned {loan.quantity_returned}) of {loan.item_id.name}")

        # record information about the kumon centre
        self.add_heading("Kumon centre", 1)
        centre = CenterDetails.objects.get()
        self.add_key_value_pair("Centre name", centre.name)
        self.add_key_value_pair("Telephone number", centre.phone_number)

        self.add_heading("Address", 2),
        self.add_key_value_pair("Line one", centre.address.line_one),
        self.add_key_value_pair("Line two", centre.address.line_two),
        self.add_key_value_pair("Line three", centre.address.line_three),
        self.add_key_value_pair("City/Town", centre.address.city_town),
        self.add_key_value_pair("Province/District",
                                centre.address.province_district),
        self.add_key_value_pair("Post code", centre.address.post_code),
        self.add_key_value_pair("Country", centre.address.country)

        # record internal technical details about the student
        self.add_heading("Technical details", 1),
        self.add_key_value_pair("K-SIS ID", str(self.student.k_sis_id)),
        self.add_key_value_pair("KMS ID", str(self.student.id))

        if self.student.deleted_at is None:
            self.add_key_value_pair("Date record deleted", "not deleted")
        else:
            self.add_key_value_pair(
                "Date record deleted", f"{self.student.deleted_at:%Y.%m.%d %H:%M:%S} (retained until {self.student.deleted_at + self.student.GDPR_RETENTION_PERIOD:%Y.%m.%d %H:%M:%S})")

        self.add_key_value_pair("Date record created",
                                self.student.created_at),
        self.add_key_value_pair("Date record modified",
                                self.student.last_modified_at)
