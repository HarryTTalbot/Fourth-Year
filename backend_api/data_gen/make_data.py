#!/usr/bin/env python3

import collections
import csv
import datetime
import itertools
import json
import random
import string
import sys

from typing import *

GRADE_TYPES = (
    ('K', 'Kindergarden'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13')
)

CLASS_NAMES = (
        "Thalia",
        "Urania",
        "Melpomene",
        "Polyhymnia",
        "Erato",
        "Calliope",
        "Clio",
        "Euterpe",
        "Terpsichore",

        "Aphrodite",
        "Apollo",
        "Ares",
        "Artemis",
        "Athena",
        "Demeter",
        "Dionysus",
        "Hades",
        "Hephaestus",
        "Hera",
        "Hermes",
        "Hestia",
        "Poseidon",
        "Zeus",

        "Coeus",
        "Crius",
        "Cronus",
        "Hyperion",
        "Iapetus",
        "Mnemosyne",
        "Oceanus",
        "Phoebe",
        "Rhea",
        "Tethys",
        "Theia",
        "Themis"
        )

this_year = datetime.date.today().year
START_DATE = datetime.date(this_year-1, 1, 1)
START_DATETIME = datetime.datetime.combine(START_DATE, datetime.time())
END_DATE = datetime.date(this_year, 12, 31)


def grouper(iterable, n, fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)


def gen_pk(used_pks):
    "given a set of used primary keys, return a pk that is not in the set and add it to the set"
    pk = max(used_pks, default=0) + 1
    used_pks.add(pk)
    return pk


def insert_address(data_out, used_pks, address):
    "insert an address into data_out"
    address_pk = gen_pk(used_pks["address"])
    data_out["backend_api.address"] += [
        {
            "id": address_pk,
            "line_one": address["StreetAddress"],
            "line_two": "",
            "line_three": "",
            "city_town": address["City"],
            "province_district": address["State"],
            "post_code": address["ZipCode"],
            "country": address["Country"]
        }
    ]
    return address_pk


def get_utc_time_str():
    "return the current date and time as a string"
    return str(datetime.datetime.now(tz=datetime.timezone.utc))


def make_data(data_file, include_staff_email=False):
    with open(data_file) as file:
        # there is some junk at the start of the data file, so skip it
        file.seek(3)
        reader = csv.DictReader(file)
        # convert `reader` to a list of dicts, each representing one row
        # in the csv
        data = list(map(dict, reader))

    # reorder the people
    random.shuffle(data)
    assert len(data) == 3000
    students, parents, staff = data[0:1200], data[1200:2400], data[2400:3000]

    # 2/3 of the parents will have a 'partner', the other 1/3 will be single
    couple_parents, single_parents = parents[:len(
        data)*2//3], data[len(data)*2//3+1:]
    couple_parents = grouper(couple_parents, n=2)
    couple_parents = tuple(map(tuple, couple_parents))
    single_parents = tuple(map(lambda p: (p,), single_parents))

    # each element of households is a tuple of 1 or 2 parents
    # each dict represents one person
    households: Tuple[Tuple[dict]]
    households = couple_parents + single_parents

    # data_out: model name -> List[Dict[field name -> value]]
    data_out = collections.defaultdict(list)
    # used_pks: model name -> Set[used primary keys]
    used_pks = collections.defaultdict(set)

    for student in students:

        date_of_birth = student["Birthday"]
        date_of_birth = date_of_birth.split("/")
        day, month, year = date_of_birth
        month, day, year = int(day), int(month), int(year)
        date_of_birth = datetime.date(year, month, day)
        date_of_birth = str(date_of_birth)

        address_pk = insert_address(data_out, used_pks, student)

        student_pk = gen_pk(used_pks["student"])
        k_sis_id = gen_pk(used_pks["k_sis_id"])

        grade = random.choice(GRADE_TYPES)[0]

        join_date = START_DATE + random.random() * (datetime.date.today() - START_DATE)
        if random.random() < 0.8:
            # 80% chance that the student is still registered in the centre
            leave_date = None
            deleted_at = None
        else:
            # 20% chance that the student has left
            leave_date = join_date + random.random() * (datetime.date.today() - join_date)

            # if the student has left, there is a 50% chance that their record
            # has been deleted
            if random.random() < 0.5:
                deleted_at = datetime.datetime.combine(leave_date, datetime.time(tzinfo=datetime.timezone.utc))
                deleted_at += datetime.timedelta(hours=random.randint(0, 24*30))
                deleted_at = str(deleted_at)
            else:
                deleted_at = None

            leave_date = str(leave_date)

        data_out["backend_api.student"] += [{
            "id": student_pk,
            "k_sis_id": k_sis_id,
            "first_name": student["GivenName"],
            "middle_name": student["MiddleInitial"] + ".",
            "last_name": student["Surname"],
            "date_of_birth": date_of_birth,
            "join_date": str(join_date),
            "leave_date": leave_date,
            "phone_number": student["TelephoneNumber"],
            "address": address_pk,
            "school": student["Company"] + " School",
            "grade": grade,
            "email": student["EmailAddress"],
            "deleted_at": deleted_at,
        }]

    job_titles = ("instructor", "administrator", "manager")

    for staff_member in staff:

        # same way of generating join and leave dates as we used for students
        join_date = START_DATE + random.random() * (datetime.date.today() - START_DATE)
        if random.random() < 0.8:
            leave_date = None
            deleted_at = None
        else:
            leave_date = join_date + random.random() * (datetime.date.today() - join_date)

            if random.random() < 0.5:
                deleted_at = datetime.datetime.combine(leave_date, datetime.time(tzinfo=datetime.timezone.utc))
                deleted_at += datetime.timedelta(hours=random.randint(0, 24*30))
                deleted_at = str(deleted_at)
            else:
                deleted_at = None

            leave_date = str(leave_date)

        data_out["backend_api.staff"] += [
                {
                    "id": gen_pk(used_pks["staff"]),
                    "first_name": staff_member["GivenName"],
                    "middle_name": staff_member["MiddleInitial"] + ".",
                    "last_name": staff_member["Surname"],
                    "job_title": random.choice(job_titles),
                    "join_date": str(join_date),
                    "leave_date": leave_date,
                    "user": None,
                    "deleted_at": deleted_at
                    }
                ]

        # backend_api.staff._email isn't part of the model, this is used
        # by the dummy data generator to assign email addresses to staff
        # accounts and is then removed
        if include_staff_email:
            data_out["backend_api.staff"][-1]["_email"] = staff_member["EmailAddress"]
            data_out["backend_api.staff"][-1]["_username"] = staff_member["Username"]
            data_out["backend_api.staff"][-1]["_password"] = staff_member["Password"]

    # generate one class for every 10 students
    for cls in range(len(students) // 10):
        class_name = random.choice(CLASS_NAMES)
        class_id = gen_pk(used_pks["class"])

        data_out["backend_api.class"] += [{
            "id": class_id,
            "name": class_name
        }]

    for student in data_out["backend_api.student"]:
        # add each student to 1 to 5 classes
        student_pk = student["id"]
        for class_pk in random.sample(data_out["backend_api.class"], k=random.randint(1, 5)):
            class_pk = class_pk["id"]

            data_out["backend_api.class_student"] += [{
                "student": student_pk,
                "class_fk": class_pk
            }]

        # assign each student to a household and add some contact details
        student_household = random.choice(households)
        num_contacts = random.randint(1, len(student_household))
        for contact in random.sample(student_household, k=num_contacts):
            contact_pk = gen_pk(used_pks["contact_detail"])
            contact_address_pk = insert_address(data_out, used_pks, contact)

            if contact["Gender"] == "male":
                relationship = random.choices(

                    population=("Father", "Uncle", "Grandfather"),
                    weights=(8, 1, 1),
                    k=1
                )[0]
            elif contact["Gender"] == "female":
                relationship = random.choices(
                    population=("Mother", "Aunt", "Grandmother"),
                    weights=(8, 1, 1),
                    k=1
                )[0]
            else:
                # ???
                relationship = "Parent"

            data_out["backend_api.contact_detail"] += [{
                "id": contact_pk,
                "first_name": contact["GivenName"],
                "middle_name": contact["MiddleInitial"] + ".",
                "last_name": contact["Surname"],
                "address": random.choice((contact_address_pk, address_pk)),
                "phone_home": "",
                "phone_business": "",
                "phone_mobile": contact["TelephoneNumber"],
                "email": contact["EmailAddress"]
            }]

            data_out["backend_api.student_contact"] += [{
                "student_id": student_pk,
                "contact_id": contact_pk,
                "relationship": relationship
            }]

    # insert subjects subject-levels
    subjects = ("Necromancy", "Astronomy", "Archaeology", "Philately", "Basket-weaving", "Forestry", "Animal husbandry", "Albanian language", "Mediæval French poetry", "Calligraphy", "Ballet", "Freudian psychoanalysis", "Contemporary Californian viticulture", "Maritime engineering", "Interpretive taxidermy", "Hot air balloon piloting", "Bankruptcy law", "Differential geometry", "Dentistry")
    for subject in subjects:
        subject_pk = gen_pk(used_pks["subject"])
        data_out["backend_api.subject"] += [
            {
                "id": subject_pk,
                "name": subject
            }
        ]
        data_out["backend_api.subject_level"] += [
            {
                "id": gen_pk(used_pks["subject_level"]),
                "subject": subject_pk,
                "name": level
            } for level, _ in GRADE_TYPES
        ]

    # generate some random LTAs
    lta_reasons = ("Illness/Injury", "Personal Circumstances", "Bereavement", "Holiday", "Other (Hates Kumon)")
    for _ in range(2000):
        student = random.choice(data_out["backend_api.student"])["id"]
        start_date = START_DATE + (END_DATE - START_DATE) * random.random()
        end_date = start_date + datetime.timedelta(days=random.randint(1, 100))
        reason = random.choice(lta_reasons)

        data_out["backend_api.longtermabsence"] += [
                {
                    "id": gen_pk(used_pks["longtermabsence"]),
                    "student": student,
                    "start_date": str(start_date),
                    "end_date": str(end_date),
                    "reason": reason
                    }
                ]

    def has_lta(student, date):
        "check if student `student` has an LTA on `date`"
        # formatting dates as YYYY-mm-dd, as datetime.date.__str__ does, means
        # we can get correct results using lexical comparison
        date = str(date)
        for lta in data_out["backend_api.longtermabsence"]:
            if lta["student"] == student and lta["start_date"] <= date and lta["end_date"] >= date:
                return True
        return False

    def add_lesson(date):
        start_time_hour = random.choice((15, 16, 17, 18))
        start_time_minute  = random.choice(range(0, 60, 5))
        start_time = datetime.time(start_time_hour, start_time_minute)
        duration = random.choice(range(30, 120, 5))
        duration = datetime.timedelta(minutes=duration)

        start_datetime = datetime.datetime.combine(date, start_time)
        start_datetime = start_datetime.astimezone(datetime.timezone.utc)
        end_datetime = start_datetime + duration
        end_datetime = end_datetime.astimezone(datetime.timezone.utc)

        class_fk = random.choice(data_out["backend_api.class"])["id"]
        subject_level = random.choice(data_out["backend_api.subject_level"])["id"]

        lesson_pk = gen_pk(used_pks["lesson"])

        data_out["backend_api.lesson"] += [
                {
                    "id": lesson_pk,
                    "start_datetime": str(start_datetime),
                    "end_datetime": str(end_datetime),
                    "class_fk": class_fk,
                    "subject_level": subject_level
                    }
                ]

        # if the class occurred in the past, generate attendance
        if end_datetime < datetime.datetime.now(tz=datetime.timezone.utc):

            for class_student in data_out["backend_api.class_student"]:
                if class_student["class_fk"] == class_fk:

                    if has_lta(class_student["student"], date):
                        status = random.choices(("P", "L", "A"), weights=[2, 2, 100])[0]
                    else:
                        status = random.choices(("P", "L", "U"), weights=[100, 5, 5])[0]

                    data_out["backend_api.attendance"] += [
                            {
                                "id": gen_pk(used_pks["attendance"]),
                                "lesson": lesson_pk,
                                "student": class_student["student"],
                                "status": status
                                }
                            ]

    # weekdays is a list of every weekday between START_DATE and END_DATE
    weekdays = []
    next_day = START_DATE
    while not weekdays or weekdays[-1] < END_DATE:
        if next_day.weekday() not in (5, 6):
            weekdays += [next_day]
        next_day += datetime.timedelta(days=1)

    for _ in range(2000):
        date = random.choice(weekdays)
        add_lesson(date)

    # add bulk itmes and bulk item logs
    bulk_items = ("Pencil", "Scalpel", "Paintbrush", "Spatula")
    for item in bulk_items:
        item_id = gen_pk(used_pks["bulkitem"])
        data_out["backend_api.bulkitem"] += [
                {
                    "id": item_id,
                    "name": item,
                    "quantity": random.randint(1, 1000)
                    }
                ]

        for _ in range(100):
            staff_id = random.choice(data_out["backend_api.staff"])["id"]
            data_out["backend_api.bulkitemlog"] += [
                    {
                        "item_id": item_id,
                        "staff_id": staff_id,
                        "type": random.choice(("W", "R")),
                        "quantity": random.randint(1, 100)
                        }
                    ]

    # for each subject-level add 5 to 15 worksheets logs and 3 worksheet logs
    for subject_level in data_out["backend_api.subject_level"]:
        for i in range(random.randint(5, 15)):
            worksheet_id = gen_pk(used_pks["worksheet"])
            data_out["backend_api.worksheet"] += [
                    {
                        "id": worksheet_id,
                        "subject_level": subject_level["id"],
                        "set": f"Problem set {i+1}",
                        "quantity": random.randint(1, 100)
                        }
                    ]

            for _ in range(3):
                staff_id = random.choice(data_out["backend_api.staff"])["id"]
                data_out["backend_api.worksheetlog"] += [
                        {
                            "worksheet_id": worksheet_id,
                            "staff_id": staff_id,
                            "type": random.choice(("W", "R")),
                            "quantity": random.randint(1, 100)
                            }
                        ]

    lendable_items = ("Industrial Society and Its Future by Ted Kaczynski", "Catechism of the Catholic Church")
    for item in lendable_items:
        item_id = gen_pk(used_pks["lendableitem"])
        data_out["backend_api.lendableitem"] += [
                {
                    "id": item_id,
                    "name": item,
                    "quantity_available": random.randint(10, 50)
                    }
                ]

        # add 5 ongoing loans for each item
        for _ in range(5):
            student_id = random.choice(data_out["backend_api.student"])["id"]
            data_out["backend_api.itemloan"] += [
                    {
                        "id": gen_pk(used_pks["itemloan"]),
                        "item_id": item_id,
                        "student_id": student_id,
                        "quantity": random.randint(1, 3)
                        }
                    ]
        # add 100 historical loans for each item
        for _ in range(100):
            student_id = random.choice(data_out["backend_api.student"])["id"]
            quantity_leant = random.randint(1, 3)
            quantity_returned = random.choices([quantity_leant-1, quantity_leant, quantity_leant+1], weights=[1,9,1])[0]
            loan_datetime = START_DATETIME + random.random() * (datetime.datetime.now() - START_DATETIME)
            loan_datetime = loan_datetime.astimezone(datetime.timezone.utc)
            data_out["backend_api.itemloanlog"] += [
                    {
                        "id": gen_pk(used_pks["itemloanlog"]),
                        "item_id": item_id,
                        "student_id": student_id,
                        "quantity_lent": quantity_leant,
                        "quantity_returned": quantity_returned,
                        "loan_datetime": str(loan_datetime)
                        }
                    ]

    # add the details of the kumon centre
    address = {
            "StreetAddress": "6 Lord Bhattacharyya Way",
            "City": "Coventry",
            "State": "",
            "ZipCode": "CV4 7EZ",
            "Country": "United Kingdom"
            }

    address_pk = insert_address(data_out, used_pks, address)

    # add created_at and last_modified_at fields to all of the models
    for items in data_out.values():
        for item in items:
            item["created_at"] = get_utc_time_str()
            item["last_modified_at"] = get_utc_time_str()

    # centre details do not have these fields so we add this after
    data_out["backend_api.centerdetails"] += [
            {
                "name": "Michael's Gale-Force Six",
                "phone_number": "+44 1234 567890",
                "address": address_pk
                }
            ]

    return data_out

def get_formatted_data(data_file, include_staff_email=False):
    data_raw = make_data(data_file, include_staff_email)

    data = []
    used_pks = collections.defaultdict(set)

    # transform the data generated data into the exact format that
    # Django expects
    for model, values in data_raw.items():
        for value in values:
            data += [
                {
                    "model": model,
                    "pk": value.get("id", gen_pk(used_pks[model])),
                    "fields": value
                }
            ]

    return data

if __name__ == "__main__":

    data = get_formatted_data("FakeNameGenerator.com_a0b42998/FakeNameGenerator.com_a0b42998.csv")

    print(f"Generated {len(data)} objects", file=sys.stderr)

    print(json.dumps(data))
