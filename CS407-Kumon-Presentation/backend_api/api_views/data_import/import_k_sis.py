import datetime
import pandas as pd
from django.db import transaction

from backend_api.api_views.students.models import *

# Method to read an excel spreadsheet and convert its contents to a numpy array


def read_file(file_path):
    data = pd.read_excel(file_path, engine='openpyxl')

    # Convert the Pandas dataframe to numpy array
    data = data.to_numpy()

    return data

# Pre-requisits:
#  - data input is in the form of a 2d array/list
#  - data input is in the form outputted by k-sis


def import_k_sis(file_path) -> (bool, str):
    # List of objects to be saved to the databse
    students = 0

    # Read the excel spreadsheet
    data = read_file(file_path)

    # Start atomic transaction (if 1 fails, all fails)
    try:
        with transaction.atomic():
            # Loop through all student records in the data
            for student_info in data:
                student = parse_student(replace_nan(student_info))
                students += 1
    except Exception as e:
        return (False, "Error with student: " + str(students+1) + ". Error Message: " + str(e))

    return (True, str(students) + " students added")

# Function to replace all "nan" values with empty strings


def replace_nan(student_info: list) -> list:
    for i in range(0, len(student_info)):
        if pd.isna(student_info[i]):
            student_info[i] = ""
    return student_info

# Method to generate a student


def parse_student(student_info: list) -> Student:
    # k_sis_id
    if student_info[0] == "":
        k_sis_id = None
    else:
        try:
            k_sis_id = int(student_info[0])
        except:
            raise ValueError("Invalid K-SIS ID Format")

    # first_name
    first_name = student_info[1]
    # middle_name
    middle_name = student_info[2]
    # last_name
    last_name = student_info[3]

    # Check name validity
    if not (first_name and last_name):
        raise ValueError("Invalid Name")

    # date_of_birth
    try:
        date_of_birth = datetime.datetime.strptime(student_info[4], "%d/%m/%Y")
    except:
        raise ValueError("Invalid Date Format (date of birth)")
    # join_date
    join_date = None
    # leave_date
    leave_date = None
    # phone_number
    phone_number = "(" + str(student_info[16]) + ") " + str(student_info[15])
    # address
    address = parse_address(student_info[8:15])
    # school
    school = student_info[7]
    # grade
    grade = student_info[5]
    # email
    email = student_info[6]

    # Check if the student already exists
    if len(Student.objects.filter(k_sis_id=k_sis_id)) == 0:
        # Create the student object
        student = Student(k_sis_id=k_sis_id, first_name=first_name,
                          middle_name=middle_name, last_name=last_name,
                          date_of_birth=date_of_birth, join_date=join_date,
                          leave_date=leave_date, phone_number=phone_number,
                          email=email, school=school, grade=grade, address=address)
    else:
        # Update student object
        student = Student.objects.get(k_sis_id=k_sis_id)
        student.first_name = first_name
        student.middle_name = middle_name
        student.last_name = last_name
        student.date_of_birth = date_of_birth
        student.phone_number = phone_number
        student.email = email
        student.school = school
        student.grade = grade
        student.address = address

    # Save the student to the database
    student.save()

    # Parse and save the mother contact details if they exist
    mother = parse_contact(student_info[17:31])

    if mother != None:
        mother_connection = Student_Contact(
            student_id=student, contact_id=mother, relationship="Mother")
        mother_connection.save()

    # Parse and save the father contact details if they exist
    father = parse_contact(student_info[31:45])

    if father != None:
        father_connection = Student_Contact(
            student_id=student, contact_id=father, relationship="Father")
        father_connection.save()

    # Parse and save the other contact details if they exist
    other = parse_contact(student_info[45:60])

    if other != None:
        other_connection = Student_Contact(
            student_id=student, contact_id=other, relationship="Other")
        other_connection.save()

    return student

# Method to generate a contact detail


def parse_contact(contact: list()):
    # Check if name fields are empty
    if contact[0] == "" or contact[2] == "":
        return None

    # first_name
    first_name = contact[0]
    # middle_name
    middle_name = contact[1]
    # last_name
    last_name = contact[2]

    # address
    address = parse_address(contact[3:10])

    # If the address is empty, dont add the contact
    if address is None:
        return None

    # phone_home
    phone_home = contact[10]
    # phone_business
    phone_business = contact[11]
    # phone_mobile
    phone_mobile = contact[12]
    # email
    email = contact[13]

    # Check if the contact detail already exists
    db = Contact_Detail.objects.filter(first_name=first_name,
                                       middle_name=middle_name, last_name=last_name, address=address,
                                       phone_home=phone_home, phone_business=phone_business,
                                       phone_mobile=phone_mobile, email=email)
    if len(db) == 1:
        return db[0]

    # Create the contact details object
    obj = Contact_Detail(first_name=first_name,
                         middle_name=middle_name, last_name=last_name, address=address,
                         phone_home=phone_home, phone_business=phone_business,
                         phone_mobile=phone_mobile, email=email)

    obj.save()

    # Return the Contact Detail (saved to the database)
    return Contact_Detail.objects.get(id=obj.id)

# Method to generate a address


def parse_address(address: list):
    # line_one
    line_one = address[0]
    # line_two
    line_two = address[1]
    # line_three
    line_three = address[2]
    # city_town
    city_town = address[3]
    # province_district
    province_district = address[4]
    # post_code
    post_code = address[5]
    # country
    country = address[6]

    # Check if address is empty
    if line_one == "" or post_code == "" or country == "":
        return None

    # Check if the address already exists
    db = Address.objects.filter(line_one=line_one, line_two=line_two,
                                line_three=line_three, city_town=city_town,
                                province_district=province_district,
                                post_code=post_code, country=country)
    if len(db) == 1:
        return db[0]

    # Create the address object
    obj = Address(line_one=line_one, line_two=line_two,
                  line_three=line_three, city_town=city_town,
                  province_district=province_district,
                  post_code=post_code, country=country)

    obj.save()

    # Return the address (saved to the database)
    return Address.objects.get(id=obj.id)
