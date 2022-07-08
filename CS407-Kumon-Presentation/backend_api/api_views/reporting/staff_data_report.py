#!/usr/bin/env python3

import datetime

from backend_api.api_views.centre_details.models import CenterDetails
from backend_api.api_views.inventory.models import BulkItemLog, WorksheetLog

from .report import Report


class StaffDataReport(Report):
    "Contains all data stored about a particular staff member"

    def __init__(self, staff):
        self.staff = staff

        name = f"{self.staff.last_name.upper()}, {self.staff.first_name}"
        if self.staff.middle_name:
            name += " " + self.staff.middle_name
        self.header_text = f"Staff Data Report: {name}"

        super().__init__()

    def populate(self):

        # add personal details
        self.add_heading("Personal details", 1),
        self.add_key_value_pair("Forename", self.staff.first_name),
        self.add_key_value_pair("Middle name(s)", self.staff.middle_name),
        self.add_key_value_pair("Surname", self.staff.last_name),
        self.add_key_value_pair("Job title", self.staff.job_title)

        # add inventory logs associated with this member of staff
        self.add_heading("Inventory logs", 1)
        self.add_heading("Bulk items", 2)
        bulk_item_logs = BulkItemLog.objects.filter(
            staff_id=self.staff).order_by("created_at")
        for log in bulk_item_logs:
            if log.type == "W":
                verb = "Withdrew"
            else:
                verb = "Restocked"
            value = f"{verb} {log.quantity} of {log.item_id.name}"
            self.add_key_value_pair(f"{log.created_at:%Y.%m.%d %H:%M}", value)

        # add worksheet logs
        self.add_heading("Worksheets", 2)
        worksheet_logs = WorksheetLog.objects.filter(
            staff_id=self.staff).order_by("created_at")
        for log in worksheet_logs:
            if log.type == "W":
                verb = "Withdrew"
            else:
                verb = "Restocked"
            value = f"{verb} {log.quantity} of {log.worksheet_id.subject_level.subject.name} ({log.worksheet_id.subject_level.name}) {log.worksheet_id.set}"
            self.add_key_value_pair(f"{log.created_at:%Y.%m.%d  %H:%M}", value)

        # add details of the kumon centre
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

        # TODO add user ID?
        # add internal technical details
        self.add_heading("Technical details", 1),
        self.add_key_value_pair("KMS ID", str(self.staff.id))

        if self.staff.deleted_at is None:
            self.add_key_value_pair("Date record deleted", "not deleted")
        else:
            self.add_key_value_pair(
                "Date record deleted", f"{self.staff.deleted_at:%Y.%m.%d %H:%M:%S} (retained until {self.staff.deleted_at + self.staff.GDPR_RETENTION_PERIOD:%Y.%m.%d %H:%M:%S})")

        self.add_key_value_pair("Date record created", self.staff.created_at),
        self.add_key_value_pair("Date record modified",
                                self.staff.last_modified_at)
