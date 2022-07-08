# Dummy data generator

An overview of what is in this directory:
 * `FakeNameGenerator.com_...` contains the raw data that is used to by the data generator
 * `loaddata.py` is a script that flushes the database and populates it with freshly generated data. Use the argument `--password` to set the password of the root user and `--save-passwords` to save every staff member's username and password to `staff-passwords.csv`
 * `make_data.py` contains the function that generates data. If you run it on its own, it will print its output (in a JSON format that can be imported into Django directly using `manage.py`) to stdout
