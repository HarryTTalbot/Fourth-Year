#!/usr/bin/env python3

import functools
from typing import Any, Callable

from fpdf import FPDF

from .student_data_report import StudentDataReport
from .staff_data_report import StaffDataReport
from .attendance_sheet import AttendanceSheet
from .record_sheet import RecordSheet

# https://pyfpdf.readthedocs.io/en/latest/reference/output/index.html
# latin-1 encoding is required because ¯\_(ツ)_/¯
def encode_pdf(pdf_generator: Callable[Any, FPDF]
    ) -> Callable[Any, bytes]:
    "convert an FPDF returned by a function to bytes"

    @functools.wraps(pdf_generator)
    def wrapper(*args, **kwargs):
        pdf = pdf_generator(*args, **kwargs)
        return pdf.output(dest="S").encode("latin-1")

    return wrapper


@encode_pdf
def get_student_data_report(student):
    pdf = StudentDataReport(student=student)
    return pdf

@encode_pdf
def get_staff_data_report(staff):
    pdf = StaffDataReport(staff=staff)
    return pdf

@encode_pdf
def get_attendance_sheet(lesson):
    pdf = AttendanceSheet(lesson=lesson)
    return pdf

@encode_pdf
def get_record_sheet(start_date, num_days=7, sheets_per_day=1, students=(None,), subject_level=None, completion_time=45):
    pdf = RecordSheet(
            start_date=start_date,
            num_days=num_days,
            sheets_per_day=sheets_per_day,
            students=students,
            subject_level=subject_level,
            completion_time=completion_time
            )
    return pdf
