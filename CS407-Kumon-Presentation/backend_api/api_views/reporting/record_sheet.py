#!/usr/bin/env python3

import collections
import datetime

from .report import Report

class RecordSheet(Report):
    "A sheet for recording the marks for at-home assignments"

    def __init__(self, start_date, num_days=7, sheets_per_day=1, students=(None,), subject_level=None, completion_time=45):

        self.start_date = start_date
        self.num_days = num_days
        self.sheets_per_day = sheets_per_day
        self.students = students
        self.subject_level = subject_level
        self.completion_time = completion_time

        self.header_text = "Kumon Record Sheet"

        super().__init__()

    def populate(self):

        first_page = True

        for student in self.students:
            # start a new page for each student unless this is the first
            if first_page:
                first_page = False
            else:
                self.add_page()

            # add student's name or a field for writing it in
            if student is None:
                self.add_handwritten_field("Name")
            else:
                name = f"{student.last_name.upper()}, {student.first_name}"
                if student.middle_name:
                    name += " " + student.middle_name
                self.add_key_value_pair("Name", name)

            # add subject and level or a field for writing it in
            if self.subject_level is None:
                self.add_handwritten_field("Subject")
                self.add_handwritten_field("Level")
            else:
                self.add_key_value_pair("Subject", str(self.subject_level.subject))
                self.add_key_value_pair("Level", self.subject_level.name)

            # add a table for scores and the standard completion time
            self.ln()
            self.add_scores_table(self.start_date, self.num_days, self.sheets_per_day)

            self.add_key_value_pair("Standard completion time (min/sheet)", str(self.completion_time))

            self.ln()
            self.add_text_box(70)
            self.add_text_box(70)
