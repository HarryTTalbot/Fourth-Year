from django.test import TestCase
import datetime
import pandas as pd
import numpy as np
import os
from django.test import Client

from backend_api.data_import.import_k_sis import *
from django.conf import settings


class Test_K_SIS_Import(TestCase):

    # Tests aiming to validate the parse address method
    def test_parse_address_positive(self):
        # ------------------------------------------------------------------------------------------------------ #
        # Positive Test Case - Full Address
        input = ["12 Zebra Street", "Elephant Zone", "Lion Area",
                 "Coventry", "West Midlands", "CV3 7FS", "United Kingdom"]

        try:
            output = parse_address(input)
        except:
            assert False  # Error in execution

        # Check fields are correct
        self.assertEqual(output.line_one, input[0])
        self.assertEqual(output.line_two, input[1])
        self.assertEqual(output.line_three, input[2])
        self.assertEqual(output.city_town, input[3])
        self.assertEqual(output.province_district, input[4])
        self.assertEqual(output.post_code, input[5])
        self.assertEqual(output.country, input[6])

        # ------------------------------------------------------------------------------------------------------ #
        # Positive Test Case - Some Fields Missing (Empty String)
        input = ["12 Zebra Street", "", "", "",
                 "", "CV3 7FS", "United Kingdom"]

        try:
            output = parse_address(input)
        except:
            assert False  # Error in execution

        # Check fields are correct
        self.assertEqual(output.line_one, input[0])
        self.assertEqual(output.line_two, input[1])
        self.assertEqual(output.line_three, input[2])
        self.assertEqual(output.city_town, input[3])
        self.assertEqual(output.province_district, input[4])
        self.assertEqual(output.post_code, input[5])
        self.assertEqual(output.country, input[6])

        # ------------------------------------------------------------------------------------------------------ #
        # Positive Test Case - Longest Possible Field Values
        input = ["100 St Martin-in-the-Fields Church Path", "110 St Martin-in-the-Fields Church Path", "101 St Martin-in-the-Fields Church Path",
                 "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch", "111 St Martin-in-the-Fields Church Path", "CH5 3QW", "The United Kingdom of Great Britain and Northern Ireland"]

        try:
            output = parse_address(input)
        except:
            assert False  # Error in execution

        # Check fields are correct
        self.assertEqual(output.line_one, input[0])
        self.assertEqual(output.line_two, input[1])
        self.assertEqual(output.line_three, input[2])
        self.assertEqual(output.city_town, input[3])
        self.assertEqual(output.province_district, input[4])
        self.assertEqual(output.post_code, input[5])
        self.assertEqual(output.country, input[6])

        # ------------------------------------------------------------------------------------------------------ #
        # Positive Test Case - Not all fields being string type
        input = [1, "Path", "", "Coventry", "", "CV3 7FS", "United Kingdom"]

        try:
            output = parse_address(input)
        except:
            assert False  # Error in execution

        # Check fields are correct
        self.assertEqual(output.line_one, str(input[0]))
        self.assertEqual(output.line_two, input[1])
        self.assertEqual(output.line_three, input[2])
        self.assertEqual(output.city_town, input[3])
        self.assertEqual(output.province_district, input[4])
        self.assertEqual(output.post_code, input[5])
        self.assertEqual(output.country, input[6])

        # ------------------------------------------------------------------------------------------------------ #
        # Positive Test Case - No Address (Empty Fields)
        input = ["", "", "", "", "", "", ""]

        try:
            output = parse_address(input)
        except:
            assert False  # Error in execution

        # Check output is None (no address)
        self.assertEqual(output, None)

    # Tests aiming to validate the parse address method
    def test_parse_address_negative(self):
        # ------------------------------------------------------------------------------------------------------ #
        # Negative Test Case - Missing Required fields (empty string) (loop to check each one separately)
        input = ["12 Zebra Street", "Elephant Zone", "Lion Area",
                 "Coventry", "West Midlands", "CV3 7FS", "United Kingdom"]
        missing = [0, 1, 3, 5, 6]

        for exclude in missing:
            # Create a new input list which replaces the missing value with an empty string
            new_input = input
            new_input[exclude] = ""

            try:
                output = parse_address(new_input)
                assert False  # No error in execution
            except:
                assert True

        # ------------------------------------------------------------------------------------------------------ #
        # Negative Test Case - Missing Required fields (null value) (loop to check each one separately)
        input = ["12 Zebra Street", "Elephant Zone", "Lion Area",
                 "Coventry", "West Midlands", "CV3 7FS", "United Kingdom"]
        missing = [0, 1, 3, 5, 6]

        for exclude in missing:
            # Create a new input list which replaces the missing value with None
            new_input = input
            new_input[exclude] = None

            try:
                output = parse_address(new_input)
                assert False  # No error in execution
            except:
                assert True

    # Tests aiming to validate the parse contact method (Does not check address)
    def test_parse_contact_positive(self):
        valid_address = ["12 Zebra Street", "Elephant Zone",
                         "", "Coventry", "", "CV3 7FS", "United Kingdom"]

        # ------------------------------------------------------------------------------------------------------ #
        # Positive Test Case - Full Contact
        input = ["Steven", "Harris", "Smith", "0777777777",
                 "0777777777", "0777777777", "steven.smith@smiths.co.uk"]
        input[3:3] = valid_address

        try:
            output = parse_contact(input)
        except:
            assert False  # Error in execution

        # Check fields are correct
        self.assertEqual(output.first_name, input[0])
        self.assertEqual(output.middle_name, input[1])
        self.assertEqual(output.last_name, input[2])
        self.assertEqual(output.phone_home, input[10])
        self.assertEqual(output.phone_business, input[11])
        self.assertEqual(output.phone_mobile, input[12])
        self.assertEqual(output.email, input[13])

        # ------------------------------------------------------------------------------------------------------ #
        # Positive Test Case - Missing some fields (empty string)
        input = ["Steven", "", "Smith", "", "",
                 "0777777777", "steven.smith@smiths.co.uk"]
        input[3:3] = valid_address

        try:
            output = parse_contact(input)
        except:
            assert False  # Error in execution

        # Check fields are correct
        self.assertEqual(output.first_name, input[0])
        self.assertEqual(output.middle_name, input[1])
        self.assertEqual(output.last_name, input[2])
        self.assertEqual(output.phone_home, input[10])
        self.assertEqual(output.phone_business, input[11])
        self.assertEqual(output.phone_mobile, input[12])
        self.assertEqual(output.email, input[13])

        # ------------------------------------------------------------------------------------------------------ #
        # Positive Test Case - No Contact Detail (Empty Fields)
        input = ["", "", "", "", "", "", "", "", "", "", "", "", "", ""]

        try:
            output = parse_contact(input)
        except:
            assert False  # Error in execution

        # Check output is None (no contact)
        self.assertEqual(output, None)

    # Tests aiming to validate the parse contact method (Does not check address)
    def test_parse_contact_negative(self):
        valid_address = ["12 Zebra Street", "Elephant Zone",
                         "", "Coventry", "", "CV3 7FS", "United Kingdom"]

        # ------------------------------------------------------------------------------------------------------ #
        # Negative Test Case - Missing Required fields (empty string) (loop to check each one separately)
        input = ["Steven", "Harris", "Smith", "0777777777",
                 "0777777777", "0777777777", "steven.smith@smiths.co.uk"]
        input[3:3] = valid_address
        missing = [0, 3, 12, 13]

        for exclude in missing:
            # Create a new input list which replaces the missing value with an empty string
            new_input = input
            new_input[exclude] = ""

            try:
                output = parse_contact(new_input)
                assert False  # No error in execution
            except:
                assert True

        # ------------------------------------------------------------------------------------------------------ #
        # Negative Test Case - Missing Required fields (null value) (loop to check each one separately)
        input = ["Steven", "Harris", "Smith", "0777777777",
                 "0777777777", "0777777777", "steven.smith@smiths.co.uk"]
        input[3:3] = valid_address
        missing = [0, 3, 12, 13]

        for exclude in missing:
            # Create a new input list which replaces the missing value with None
            new_input = input
            new_input[exclude] = None

            try:
                output = parse_contact(new_input)
                assert False  # No error in execution
            except:
                assert True

        # ------------------------------------------------------------------------------------------------------ #
        # Negative Test Case - Missing Address (Empty)
        input = ["Steven", "Harris", "Smith", "0777777777",
                 "0777777777", "0777777777", "steven.smith@smiths.co.uk"]
        input[3:3] = ["", "", "", "", "", "", ""]
        missing = [0, 3, 12, 13]

        for exclude in missing:
            # Create a new input list which replaces the missing value with None
            new_input = input
            new_input[exclude] = None

            try:
                output = parse_contact(new_input)
                assert False  # No error in execution
            except:
                assert True

    # Tests aiming to validate that addresses are correctly added to contact details created
    def test_contact_address_relations(self):
        # ------------------------------------------------------------------------------------------------------ #
        # Positive Test Case
        valid_address = ["12 Zebra Street", "Elephant Zone",
                         "", "Coventry", "", "CV3 7FS", "United Kingdom"]
        input = ["Steven", "Harris", "Smith", "0777777777",
                 "0777777777", "0777777777", "steven.smith@smiths.co.uk"]
        input[3:3] = valid_address

        try:
            output = parse_contact(input)
        except:
            assert False  # Error in execution

        # Check the address (Field by field due to hidden id and timestamp fields)
        self.assertEqual(output.address.line_one, valid_address[0])
        self.assertEqual(output.address.line_two, valid_address[1])
        self.assertEqual(output.address.line_three, valid_address[2])
        self.assertEqual(output.address.city_town, valid_address[3])
        self.assertEqual(output.address.province_district, valid_address[4])
        self.assertEqual(output.address.post_code, valid_address[5])
        self.assertEqual(output.address.country, valid_address[6])

        # ------------------------------------------------------------------------------------------------------ #
        # Positive Test Case - 2 contacts with same address should have same address object
        input = ["Molly", "Deliah", "Smith", "0777777777",
                 "0777777777", "0777777777", "Molly.smith@smiths.co.uk"]
        input[3:3] = valid_address

        try:
            output2 = parse_contact(input)
        except:
            assert False  # Error in execution

        # Check the address has the same address as in first test case
        self.assertEqual(output2.address.id, output.address.id)

    # Tests aiming to validate that student details are correctly parsed
    def test_parse_student_positive(self):
        valid_address = ["12 Zebra Street", "Elephant Zone",
                         "", "Coventry", "", "CV3 7FS", "United Kingdom"]
        valid_contact = ["", "", "", "", "",
                         "", "", "", "", "", "", "", "", ""]

        # ------------------------------------------------------------------------------------------------------ #
        # Positive Test Case - Full Student
        input = ["12345678", "Steven", "Harris", "Smith", "19/01/1998", 1,
                 "steven.smith@smiths.co.uk", "Pandas Academy of Maths", "0777777777", "44"]
        input[8:8] = valid_address
        input[17:17] = valid_contact
        input[31:31] = valid_contact
        input[45:45] = valid_contact

        try:
            student = parse_student(input)
        except:
            assert False  # Error in execution

        # Check the student fields (Field by field due to hidden id and timestamp fields)
        self.assertEqual(str(student.k_sis_id), input[0])
        self.assertEqual(student.first_name, input[1])
        self.assertEqual(student.middle_name, input[2])
        self.assertEqual(student.last_name, input[3])
        self.assertEqual(student.date_of_birth.strftime("%d/%m/%Y"), input[4])
        self.assertEqual(student.grade, input[5])
        self.assertEqual(student.email, input[6])
        self.assertEqual(student.school, input[7])
        self.assertEqual(student.phone_number,
                         "(" + input[16] + ") " + input[15])

        # ------------------------------------------------------------------------------------------------------ #
        # Positive Test Case - Missing some fields (empty string)
        input = ["", "Steven", "", "Smith", "19/01/1998", 1,
                 "steven.smith@smiths.co.uk", "Pandas Academy of Maths", "0777777777", "44"]
        input[8:8] = valid_address
        input[17:17] = valid_contact
        input[31:31] = valid_contact
        input[45:45] = valid_contact

        try:
            student = parse_student(input)
        except:
            assert False  # Error in execution

        # Check the student fields (Field by field due to hidden id and timestamp fields)
        self.assertEqual(student.k_sis_id, None)
        self.assertEqual(student.first_name, input[1])
        self.assertEqual(student.middle_name, input[2])
        self.assertEqual(student.last_name, input[3])
        self.assertEqual(student.date_of_birth.strftime("%d/%m/%Y"), input[4])
        self.assertEqual(student.grade, input[5])
        self.assertEqual(student.email, input[6])
        self.assertEqual(student.school, input[7])
        self.assertEqual(student.phone_number,
                         "(" + input[16] + ") " + input[15])

        # ------------------------------------------------------------------------------------------------------ #
        # Positive Test Case - "K" as a grade
        input = ["", "Steven", "", "Smith", "19/01/1998", 'K',
                 "steven.smith@smiths.co.uk", "Pandas Academy of Maths", "0777777777", "44"]
        input[8:8] = valid_address
        input[17:17] = valid_contact
        input[31:31] = valid_contact
        input[45:45] = valid_contact

        try:
            student = parse_student(input)
        except:
            assert False  # Error in execution

        # Check the student fields (Field by field due to hidden id and timestamp fields)
        self.assertEqual(student.k_sis_id, None)
        self.assertEqual(student.first_name, input[1])
        self.assertEqual(student.middle_name, input[2])
        self.assertEqual(student.last_name, input[3])
        self.assertEqual(student.date_of_birth.strftime("%d/%m/%Y"), input[4])
        self.assertEqual(student.grade, input[5])
        self.assertEqual(student.email, input[6])
        self.assertEqual(student.school, input[7])
        self.assertEqual(student.phone_number,
                         "(" + input[16] + ") " + input[15])

    # Tests aiming to validate that student details are correctly parsed
    def test_parse_student_negative(self):
        valid_address = ["12 Zebra Street", "Elephant Zone",
                         "", "Coventry", "", "CV3 7FS", "United Kingdom"]
        valid_contact = ["", "", "", "", "",
                         "", "", "", "", "", "", "", "", ""]

        # ------------------------------------------------------------------------------------------------------ #
        # Negative Test Case - Missing Required fields (empty string) (loop to check each one separately)
        input = ["12345678", "Steven", "Harris", "Smith", "19/01/1998", 1,
                 "steven.smith@smiths.co.uk", "Pandas Academy of Maths", "0777777777", "44"]
        input[8:8] = valid_address
        input[17:17] = valid_contact
        input[31:31] = valid_contact
        input[45:45] = valid_contact

        missing = [1, 3, 4, 5, 6, 7, 15, 16]

        for exclude in missing:
            # Create a new input list which replaces the missing value with an empty string
            new_input = input
            new_input[exclude] = ""

            try:
                success, output = parse_student(new_input)
                assert False  # No error in execution
            except:
                assert True  # Error in execution

        # ------------------------------------------------------------------------------------------------------ #
        # Negative Test Case - Missing Required fields (null value) (loop to check each one separately)
        for exclude in missing:
            # Create a new input list which replaces the missing value with None
            new_input = input
            new_input[exclude] = None

            try:
                success, output = parse_student(new_input)
                assert False  # No error in execution
            except:
                assert True  # Error in execution

        # ------------------------------------------------------------------------------------------------------ #
        # Negative Test Case - Incorrect grade value
        # Create a new input list which replaces the grade value
        new_input = input
        new_input[5] = 14

        try:
            success, output = parse_student(input)
            assert False  # No error in execution
        except:
            assert True  # Error in execution

    # Tests aiming to validate that addresses and students are correctly linked
    def test_student_address_relations(self):
        # ------------------------------------------------------------------------------------------------------ #
        # Positive Test Case
        valid_address = ["12 Zebra Street", "Elephant Zone",
                         "", "Coventry", "", "CV3 7FS", "United Kingdom"]
        valid_contact = ["", "", "", "", "",
                         "", "", "", "", "", "", "", "", ""]
        input = ["12345678", "Steven", "Harris", "Smith", "19/01/1998", 1,
                 "steven.smith@smiths.co.uk", "Pandas Academy of Maths", "0777777777", "44"]
        input[8:8] = valid_address
        input[17:17] = valid_contact
        input[31:31] = valid_contact
        input[45:45] = valid_contact

        try:
            student = parse_student(input)
        except:
            assert False  # Error in execution

        # Check the address (Field by field due to hidden id and timestamp fields)
        self.assertEqual(student.address.line_one, valid_address[0])
        self.assertEqual(student.address.line_two, valid_address[1])
        self.assertEqual(student.address.line_three, valid_address[2])
        self.assertEqual(student.address.city_town, valid_address[3])
        self.assertEqual(student.address.province_district, valid_address[4])
        self.assertEqual(student.address.post_code, valid_address[5])
        self.assertEqual(student.address.country, valid_address[6])

        # ------------------------------------------------------------------------------------------------------ #
        # Positive Test Case - 2 contacts with same address should have same address object
        input = ["12345679", "Molly", "Harris", "Smith", "19/01/1998", 1,
                 "molly.smith@smiths.co.uk", "Pandas Academy of Maths", "0777777777", "44"]
        input[8:8] = valid_address
        input[17:17] = valid_contact
        input[31:31] = valid_contact
        input[45:45] = valid_contact

        try:
            student2 = parse_student(input)
        except:
            assert False  # Error in execution

        # Check the address has the same address as in first test case
        self.assertEqual(student2.address.id, student.address.id)

    # Tests aiming to validate that students and contacts are correctly linked
    def test_student_contact_relations(self):
        # ------------------------------------------------------------------------------------------------------ #
        # Positive Test Case
        valid_address = ["12 Zebra Street", "Elephant Zone",
                         "", "Coventry", "", "CV3 7FS", "United Kingdom"]
        blank_contact = ["", "", "", "", "",
                         "", "", "", "", "", "", "", "", ""]
        valid_contact = ["Steven", "Harris", "Smith", "12 Zebra Street", "Elephant Zone", "", "Coventry", "",
                         "CV3 7FS", "United Kingdom", "0777777777", "0777777777", "0777777777", "steven.smith@smiths.co.uk"]
        input = ["12345678", "Steven", "Harris", "Smith", "19/01/1998", 1,
                 "steven.smith@smiths.co.uk", "Pandas Academy of Maths", "0777777777", "44"]
        input[8:8] = valid_address
        input[17:17] = valid_contact
        input[31:31] = blank_contact
        input[45:45] = blank_contact

        try:
            student = parse_student(input)
        except:
            assert False  # Error in execution

        relationship = models.Student_Contact.objects.filter(
            student_id=student, relationship="Mother")
        mother = relationship[0].contact_id

        # Check the address (Field by field due to hidden id and timestamp fields)
        self.assertEqual(mother.first_name, valid_contact[0])
        self.assertEqual(mother.middle_name, valid_contact[1])
        self.assertEqual(mother.last_name, valid_contact[2])
        self.assertEqual(mother.phone_home, valid_contact[10])
        self.assertEqual(mother.phone_business, valid_contact[11])
        self.assertEqual(mother.phone_mobile, valid_contact[12])
        self.assertEqual(mother.email, valid_contact[13])

        # ------------------------------------------------------------------------------------------------------ #
        # Positive Test Case - 2 contacts with same address should have same address object
        input = ["12345679", "Molly", "Harris", "Smith", "19/01/1998", 1,
                 "molly.smith@smiths.co.uk", "Pandas Academy of Maths", "0777777777", "44"]
        input[8:8] = valid_address
        input[17:17] = blank_contact
        input[31:31] = valid_contact
        input[45:45] = blank_contact

        try:
            student2 = parse_student(input)
        except:
            assert False  # Error in execution

        relationship = models.Student_Contact.objects.filter(
            student_id=student2, relationship="Father")
        father = relationship[0].contact_id

        # Check the address has the same address as in first test case
        self.assertEqual(father.id, mother.id)

    # Tests aiming to validate that excel spreadsheets are correctly read
    def test_read_file(self):
        # ------------------------------------------------------------------------------------------------------ #
        # Positive Test Case - Write to excel and see if read version is the same
        # Test Array
        input = np.array([["Hi", "This", "Is", "A", "Test"], [1, 2, 3, 4, 5]])

        # Convert to dataframe
        dataframe = pd.DataFrame(data=input)

        # Write Dataframe to excel sheet
        dataframe.to_excel(r'Test.xlsx', index=False)

        # Call function to read excel sheet
        output = read_file(r'Test.xlsx')

        # Delete excel sheet
        os.remove(r'Test.xlsx')

        # Check the read version is the same as the written version
        self.assertEqual((input == output).all(), True)


"""
    # Tests aiming to validate that the api call works as expected
    def test_api_call(self):
        # Get the dummy excel file
        file = open(os.path.join(settings.BASE_DIR, "backend_api", "tests", "import_export", "dump_import_export", "test_k_sis.xlsx"))

        # Send a post request
        client = Client()
        response = client.post('/api/import/k_sis/', {"file": file, "name": "idk", "type":"k_sis"})


        # Check the status code is as expected
        self.assertEqual(response.status_code, 201)
"""
