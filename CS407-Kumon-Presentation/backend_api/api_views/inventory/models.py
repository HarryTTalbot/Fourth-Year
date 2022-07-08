from django.db import models
from backend_api.api_views.staff.models import Staff
from backend_api.api_views.students.models import Student
from backend_api.api_views.subjects.models import Subject_Level
from django_cryptography.fields import encrypt

class BulkItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} (x{self.quantity})"


class BulkItemLog(models.Model):
    item_id = models.ForeignKey(BulkItem, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=1, choices=[
                            ('W', 'Withdrawal'), ('R', 'Restock')])
    quantity = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.type} {self.quantity} of {self.item_id.name} by {self.staff_id}"


class Worksheet(models.Model):
    id = models.AutoField(primary_key=True)
    subject_level = models.ForeignKey(
        Subject_Level, null=True, on_delete=models.SET_NULL)
    set = models.CharField(max_length=50)

    quantity = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.subject_level} {self.set} (x{self.quantity})"


class WorksheetLog(models.Model):
    worksheet_id = models.ForeignKey(Worksheet, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=1, choices=[
                            ('W', 'Withdrawal'), ('R', 'Restock')])
    quantity = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.type} {self.quantity} of {self.worksheet_id.subject_level} {self.worksheet_id.set} by {self.staff_id}"


class LendableItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    quantity_available = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} (x{self.quantity_available})"


# Current Loans

class ItemLoan(models.Model):
    id = models.AutoField(primary_key=True)

    item_id = models.ForeignKey(LendableItem, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} of {self.item_id.name} loaned to {self.student_id}"


# Historical loans

class ItemLoanLog(models.Model):
    id = models.AutoField(primary_key=True)

    item_id = models.ForeignKey(
        LendableItem, null=True, on_delete=models.SET_NULL)
    student_id = models.ForeignKey(
        Student, null=True, on_delete=models.SET_NULL)

    quantity_lent = models.PositiveIntegerField()
    quantity_returned = models.PositiveIntegerField()

    loan_datetime = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity_lent} (returned {self.quantity_returned}) of {self.item_id.name} loaned to {self.student_id}"
