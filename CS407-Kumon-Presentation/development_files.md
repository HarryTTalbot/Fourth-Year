# Overview of Root File Structure

This section details what each of the files and directories are in the root directory of the project development files:

 - `backend_api` - folder containing the django application for the backend
 - `frontend` - folder containing the svelte project for the frontend website interface
 - `frontend_app` - folder containing the django application for hosting the frontend interface
 - `kumon` - folder containing the django project
 - `openapi_schema` - folder containing the auto-generated schema for the backend api
 - `build.py` - python script to package the application into an executable
 - `Dockerfile`, `docker-compose.yml` -  docker container files
 - `entrypoint.sh` - script to set up and run the django application (including migrating database changes)
 - `gui.py` - python script to run the django application alongside a chrome gui, entrypoint for the packaged application
 - `gui.spec` - specification file for the app packaging
 - `manage.py` - file to run the django server
 - `requirements.txt` - python libraries used in the development process


 # Backend Application

This is in the `backend_api` folder of the development files. The development files are split into 3 general parts `api_views`, `data_gen` and `tests`.

The root level files of this application are:
 - `admin.py` - creates the django admin interface useful for debugging 
 - `apps.py` - defines the django application and specifies startup behaviour
 - `models.py` - defines the database models used by the application
 - `serializers.py` - defines general purpose serializers used by the application
 - `urls.py` - defines endpoints by mapping views to urls
 - `views.py` - defines functionality of general purpose endpoints provided by the application

### `api_views`

The API views are split into 10 main sections:
 - `attendance` - endpoints related to managing lessons and taking attendance
 - `authentication` - endpoints related to user accounts and login system
 - `centre_details` - endpoints related to storing information on the kumon centre
 - `classes` - endpoints related to managing class membership
 - `data_import` - endpoints related to importing/exporting data from the application
 - `inventory` - endpoints related to managing the inventory of the kumon centre
 - `reporting` - endpoints related to creating reporting on students and staff data
 - `staff` - endpoints related to student administration
 - `students` - endpoints related to staff administration
 - `subjects` - endpoints related to managing the subjects taught by the kumon centre

Inside each of these folders are the following files:
 - `models.py` - defines database models relevent to a section of the application
 - `serializers.py` - defines serializers used by this section of the application
 - `tests.py` - defines unit tests for endpoints in this section of the application
 - `views.py` - defines functionality of endpoints in this section of the application

### `data_gen`

This is the data generation part of the application. It can be used to generate a dummy database designed to be used during development and testing.

The files inside of this section are:
 - `loaddata.py` - is a script that flushes the database and populates it with freshly generated data. Use the argument `--password` to set the password of the root user and `--save-passwords` to save every staff member's username and password to `staff-passwords.csv`
 - `make_data.py` - contains the function that generates data. If you run it on its own, it will print its output (in a JSON format that can be imported into Django directly using `manage.py`) to stdout

### `tests`

This is the part of the application where some of the backend tests are located.

The backend api tests for the importing and exporting part of the application are located inside of the `import_export` folder.

The file `api_test_case` defines code shared by all unit tests of api endpoints

 # Frontend Application

This is in the `frontend` folder in the development files. The frontend application is a svelte project.

The application is split into the following primary parts:
 - `kumon_app_backend_api` - this is the open api generated code to communicate with the backend api
 - `public` - static files such as the core HTML linking CSS files, and the icon
 - `src` - files written during development containing all aspects of the user interface

The frontend application depends on the other files inside of the root level of the frontend directory:
 - `Dockerfile` - Docker file for the frontend container
 - `package-lock.json`, `package.json` - Libraries requiring installation for the frontend development
 - `rollup.config.json` - Configuration file for the compilation of the frontend

### `kumon_app_backend_api`

The files for communication to the backend api. For the development there are two primary folders which are of interest. These are:
 - `src/apis` - code for each api endpoint to communicate with the backend
 - `src/models` - objects used in the apis code

### `src`

This part of the frontend application includes the source code of the front end interface. It is split into the following parts:
 - `components` - miscellaneous features utilised by each page
 - `formFields` - custom svelte code for inputting data unique to this application
 - `modals` - modals for general usage
 - `routes` - the main user interface files. Each major component is contained within its own directory.
 - `utils` - useful reusable functions
 - `App.svelte` - container file for the application
 - `api.js` - file that verifies access to the API
 - `main.js` - loader for App.svelte
 - `routes.js` - contains the addresses that the user will input and maps them to specific files
 - `sessionStorage.js` - stores the session authentication token
 - `utils.js` - provides some useful reusable functions

The source code for each page of the application can be found in the `routes` folder. Here the source code is organised in a hierarchical structure modelled on the structure of the website.

 # Frontend Hosting Application

This is in the `frontend_app` folder in the development files. This is a django application which hosts the frontend interface. It does this by taking the most recent compiled version of the frontend and including it as a template for the django application.

This django application is referenced by the host application so that when the user navigates to `localhost:8000/`, the front end interface is loaded.

The reference to the front end compiled interface is in `templates/frontend_app/svelte.html`.

 # Django Host Application

This is in the `kumon` folder in the development files. This is the main application of the django server.

It contains the following primary files:
 - `dev_settings.py` - development settings of the django server
 - `settings.py` - production environment settings of the django server
 - `urls.py` - routing of the requests sent to the django server
