from django.test import TestCase
from django.test import Client
from django.http import FileResponse

from backend_api.data_import.full import *
import os

"""

These tests do not extensively test django 'loaddata' and 'dumpdata' as these are already fully
tested django functions.

The tests here focus on the APIs constructed, inspecific passing Files in and receiving them back.

"""

class Test_Dump_Import_Export(TestCase):

    def test_export(self):
        client = Client()
        response = client.get('/api/import/export/')

        # Check that the response type is correct
        self.assertEqual(type(response) == FileResponse, True)

    def test_import(self):
        # Generate a dump file
        client = Client()
        response = client.get('/api/import/export/')

        # Get Filenames
        f = []
        for (dirpath, dirnames, filenames) in os.walk(DUMP_EXPORT_ROOT):
            f.extend(filenames)
            break

        assert len(f) > 0

        file = open(os.path.join(DUMP_EXPORT_ROOT, f[0]))

        # Send import request
        response2 = client.post('/api/import/import/', {"file": file, "name": "idk", "type":"dumps"})

        self.assertEqual(response2.status_code, 201)
