#!/usr/bin/env python3

import argparse
import json
import os
import sys
import tempfile

import django
from django.core.management import call_command
from django.core.management.commands import flush, loaddata
from django.contrib.auth.hashers import make_password

import make_data

# set up the environment

sys.path.insert(0, os.path.dirname(os.path.dirname(os.getcwd())))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kumon.settings")
os.environ.setdefault("KUMON_DEVELOPMENT", "0")
django.setup()

from backend_api.api_views.staff.models import Staff
from django.contrib.auth.models import UserManager, User

# parse command line args

parser = argparse.ArgumentParser()
parser.add_argument(
    "--password", help="Password for the root user; Django will generate a password if this is not specified")
parser.add_argument("--save-passwords", action=argparse.BooleanOptionalAction)
args = parser.parse_args()


# flush the database

cmd = flush.Command()
call_command(cmd, interactive=False)
if os.path.isfile("staff-passwords.csv"):
    os.remove("staff-passwords.csv")

print("Flushed database")

# generate data

data = make_data.get_formatted_data(
    "FakeNameGenerator.com_a0b42998/FakeNameGenerator.com_a0b42998.csv", include_staff_email=True)

print(f"Generated {len(data)} objects")

# create accounts for staff members

um = UserManager()
um.model = User

staff = [item for item in data if item["model"] == "backend_api.staff"]

used_usernames = dict()

print("Creating staff accounts")
with open("staff-passwords.csv", "a") as passwords_file:
    for item in staff:
        username = item["fields"]["_username"]
        password = item["fields"]["_password"]

        # some usernames are non-unique
        if username not in used_usernames:
            used_usernames[username] = 0
        else:
            used_usernames[username] += 1
            username += str(used_usernames[username])

        user = um.create_user(
                username=username,
                password=password,
                first_name=item["fields"]["first_name"],
                last_name=item["fields"]["last_name"],
                email=item["fields"]["_email"]
                )

        item["fields"].pop("_username")
        item["fields"].pop("_password")
        item["fields"].pop("_email")

        item["fields"]["user"] = user.pk

        if args.save_passwords:
            passwords_file.write(username + "," + password + "\n")

# set a random staff member as the root user

if args.password is not None:
    password = args.password
else:
    password = um.make_random_password(length=20)

root = um.create_superuser("root", password=password)

master_passcode = um.make_random_password(length=20)

staff[0]["fields"]["user"] = root.id
staff[0]["fields"]["passcode"] = make_password(master_passcode)

print(f"Created superuser 'root' with password {password!r}")
print(f"Set master recovery passcode to {master_passcode!r}")

# load data

cmd = loaddata.Command()
with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as tf:
    json.dump(data, tf)
    tf.seek(0)

    call_command(cmd, (str(tf.name),), verbosity=3)
