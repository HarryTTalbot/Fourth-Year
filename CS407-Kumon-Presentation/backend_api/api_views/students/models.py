from django.db import models
import datetime
from django_cryptography.fields import encrypt


class Address(models.Model):
    id = models.AutoField(primary_key=True)

    line_one = models.CharField(max_length=50)
    line_two = models.CharField(max_length=50, blank=True)
    line_three = models.CharField(max_length=50, blank=True)
    city_town = models.CharField(max_length=50, blank=True)
    province_district = models.CharField(max_length=50, blank=True)
    post_code = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        address = filter(bool, (self.country, self.province_district,
                         self.city_town, self.line_one, self.line_two, self.line_three))
        return f"{self.post_code} {', '.join(address)}"

    class Meta:
        verbose_name_plural = "Addresses"


GRADE_TYPES = (
    ('K', 'Kindergarden'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'),
    ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),
    ('11', '11'), ('12', '12'), ('13', '13')
)


class Student(models.Model):
    id = models.AutoField(primary_key=True)

    k_sis_id = models.BigIntegerField(unique=True, blank=True, null=True)

    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)

    date_of_birth = models.DateField()
    join_date = models.DateField(blank=True, null=True)
    leave_date = models.DateField(blank=True, null=True)

    phone_number = models.CharField(max_length=17)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    school = models.CharField(max_length=50)
    grade = models.CharField(max_length=2, choices=GRADE_TYPES)
    email = models.EmailField()

    deleted_at = models.DateTimeField(blank=True, null=True)
    GDPR_RETENTION_PERIOD = datetime.timedelta(days=12 * 30)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        names = filter(
            bool, (self.first_name, self.middle_name, self.last_name))
        return f"{' '.join(names)} ({self.school}, {self.grade})"


class Contact_Detail(models.Model):
    id = models.AutoField(primary_key=True)

    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)

    address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)

    phone_home = models.CharField(max_length=17, blank=True)
    phone_business = models.CharField(max_length=17, blank=True)
    phone_mobile = models.CharField(max_length=17)

    email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        names = filter(
            bool, (self.first_name, self.middle_name, self.last_name))
        return " ".join(names)


class Student_Contact(models.Model):
    id = models.AutoField(primary_key=True)

    student_id = models.ForeignKey(
        Student, related_name='contact_students', on_delete=models.CASCADE
    )

    contact_id = models.ForeignKey(
        Contact_Detail, related_name='student_contacts', on_delete=models.CASCADE
    )

    relationship = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['student_id', 'contact_id']

    def __str__(self):
        return f"{self.student_id} → {self.contact_id} ({self.relationship})"

    class Meta:
        unique_together = ['student_id', 'contact_id']
