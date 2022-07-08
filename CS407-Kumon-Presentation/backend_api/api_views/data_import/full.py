
import os
from io import StringIO
from datetime import datetime

# Django imports to run commands and access files
from django.core import management
from django.core.files.storage import FileSystemStorage

# Django imports to send a response to auto-download a file
from django.http import FileResponse
from django.http.response import HttpResponseBase

# The root directory for storing dump files
from django.conf import settings

# Method which imports a dump file into the database


def import_full(filename: str) -> (bool, str):
    # Rename the file to have the file extension .json (needed for loaddata)
    jsonName = os.path.join(settings.DUMP_IMPORT_ROOT, filename[:-6] + ".json")
    os.rename(os.path.join(settings.DUMP_IMPORT_ROOT, filename), jsonName)

    # Create a buffer to store output from loaddata command
    buffer = StringIO()

    # Call the django loaddata command to load the data from the file into the database
    management.call_command('loaddata', jsonName, exclude=['auth.permission'], format="json", stdout=buffer)

    # Moves the cursor to position 0
    buffer.seek(0)

    # Rename the file back to its original name
    os.rename(jsonName, os.path.join(settings.DUMP_IMPORT_ROOT, filename))

    # Return the success of the loading data
    return [True, buffer.read()]

# Method which creates and returns a file which includes all the data from the database


def export_full():
    # Create a string IO to mock represent a file
    buffer = StringIO()

    # Call the django dumpdata command to add the database to the file
    management.call_command('dumpdata', 'backend_api',
                            'auth', stdout=buffer, format="json")

    # Moves the cursor to position 0
    buffer.seek(0)

    # Write it to a file in the system storage
    filename = str(datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + ".kumon")

    # Open the folder in the file system to store the file
    fileSystem = FileSystemStorage(settings.DUMP_EXPORT_ROOT)

    # Check that if the dump directory doesnt exist, create it
    if not os.path.exists(settings.DUMP_EXPORT_ROOT):
        os.makedirs(settings.DUMP_EXPORT_ROOT)

    # Store the file in the file system
    fileSystem.save(filename, buffer)

    # Return the file in a http response
    response = FileResponse(fileSystem.open(
        filename, 'rb'), content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="dump-' + \
        filename + '"'

    return response
