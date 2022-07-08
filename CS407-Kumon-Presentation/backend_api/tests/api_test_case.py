from django.test import TestCase, Client

from backend_api.api_views.attendance.models import *
from backend_api.api_views.classes.models import *
from backend_api.api_views.inventory.models import *
from backend_api.api_views.staff.models import *
from backend_api.api_views.students.models import *
from backend_api.api_views.subjects.models import *


# Decorator for client http methods to strip pagination from response object
def removePagination(httpMethod):
    def newHttpMethod(self, *args, **kwargs):
        resp = httpMethod(self, *args, **kwargs)
        try:
            resp.data = resp.data.get('results', resp.data)
        except AttributeError:
            pass
        return resp
    return newHttpMethod


# Subclass of client with pagination automatically removed from all http methods
class NoPageClient(Client):
    def __new__(cls, *args, **kwargs):
        obj = super(NoPageClient, cls).__new__(cls, *args, **kwargs)
        http_methods = ['get', 'post', 'put', 'patch', 'delete']
        for m in http_methods:
            setattr(obj, m, removePagination(getattr(obj, m)))
        return obj


class APITestCase(TestCase):

    def setUp(self,):
        self.client = NoPageClient()

        self.address = Address.objects.create(
            line_one='test-l1', city_town='test-t', post_code='TE51 1ST', country='test-c'
        )
        self.student1 = Student.objects.create(
            k_sis_id=1, first_name='test-student1-f', last_name='test-student1-l',
            date_of_birth='2000-01-01', phone_number='01234567890',
            address=self.address, school='test-s', grade=1, email='test@test.com'
        )
        self.student2 = Student.objects.create(
            k_sis_id=2, first_name='test-student2-f', last_name='test-student2-l',
            date_of_birth='2000-01-01', phone_number='01234567890',
            address=self.address, school='test-s', grade=1, email='test@test.com'
        )
        self.contact1 = Contact_Detail.objects.create(
            first_name='test-contact1-f', last_name='test-contact1-l', address=self.address,
            phone_mobile='01234567890', email='test@test.com'
        )
        self.contact2 = Contact_Detail.objects.create(
            first_name='test-contact2-f', last_name='test-contact2-l', address=self.address,
            phone_mobile='01234567890', email='test@test.com'
        )
        self.student_contact = Student_Contact.objects.create(
            student_id=self.student1, contact_id=self.contact1, relationship='test-r'
        )
        self.class1 = Class.objects.create(
            name='test-class1'
        )
        self.class2 = Class.objects.create(
            name='test-class2'
        )
        self.class_student = Class_Student.objects.create(
            student=self.student1, class_fk=self.class1
        )
        self.subject1 = Subject.objects.create(
            name='test-s1'
        )
        self.subject2 = Subject.objects.create(
            name='test-s2'
        )
        self.subject_level1 = Subject_Level.objects.create(
            subject=self.subject1, name='test-s1-l1'
        )
        self.subject_level2 = Subject_Level.objects.create(
            subject=self.subject2, name='test-s2-l1'
        )
        self.lesson1 = Lesson.objects.create(
            start_datetime='2022-01-01T09:00:00Z', end_datetime='2022-01-01T10:00:00Z', class_fk=self.class1, subject_level=self.subject_level1
        )
        self.lesson2 = Lesson.objects.create(
            start_datetime='2022-02-01T09:00:00Z', end_datetime='2022-02-01T10:00:00Z', class_fk=self.class1, subject_level=self.subject_level1
        )
        self.lesson3 = Lesson.objects.create(
            start_datetime='2022-02-08T09:00:00Z', end_datetime='2022-02-08T10:00:00Z', class_fk=self.class1, subject_level=self.subject_level1
        )
        self.attedance = Attendance.objects.create(
            lesson=self.lesson1, student=self.student1, status='P'
        )
        self.long_term_absence = LongTermAbsence.objects.create(
            student=self.student1, start_date='2022-02-01', end_date='2022-02-07'
        )
        self.staff = Staff.objects.create(
            first_name='test-staff-f', last_name='test-staff-l', job_title='test-staff-j'
        )
        self.bulk_item = BulkItem.objects.create(
            name='test-b-item', quantity=10
        )
        self.bulk_item_log1 = BulkItemLog.objects.create(
            item_id=self.bulk_item, staff_id=self.staff, type='W', quantity=5
        )
        self.bulk_item_log2 = BulkItemLog.objects.create(
            item_id=self.bulk_item, staff_id=self.staff, type='R', quantity=5
        )
        self.worksheet = Worksheet.objects.create(
            subject_level=self.subject_level1, set='test-s', quantity=10
        )
        self.worksheet_log1 = WorksheetLog.objects.create(
            worksheet_id=self.worksheet, staff_id=self.staff, type='W', quantity=5
        )
        self.worksheet_log2 = WorksheetLog.objects.create(
            worksheet_id=self.worksheet, staff_id=self.staff, type='R', quantity=5
        )
        self.lendable_item1 = LendableItem.objects.create(
            name='test-l-item1', quantity_available=10
        )
        self.lendable_item2 = LendableItem.objects.create(
            name='test-l-item2', quantity_available=10
        )
        self.item_loan1 = ItemLoan.objects.create(
            item_id=self.lendable_item1, student_id=self.student1, quantity=5
        )
        self.item_loan2 = ItemLoan.objects.create(
            item_id=self.lendable_item1, student_id=self.student1, quantity=10
        )
        self.item_loan_log1 = ItemLoanLog.objects.create(
            item_id=self.lendable_item1, student_id=self.student1,
            quantity_lent=5, quantity_returned=5, loan_datetime='2022-01-01T09:00:00Z'
        )
        self.item_loan_log1 = ItemLoanLog.objects.create(
            item_id=self.lendable_item1, student_id=self.student1,
            quantity_lent=5, quantity_returned=0, loan_datetime='2022-01-02T09:00:00Z'
        )
