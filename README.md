# CS407-Kumon-App

Kumon Centre Management App for the CS407 Group Project.

## Requirements

- Python 3.10
  - On Ubuntu: `sudo apt install python3 python3-pip`
  - The full list of dependencies can be found in [`requirements.txt`](./requirements.txt).
- NodeJS 16.13.0 LTS
  - A version manager is recommended, e.g. [nvm](https://github.com/nvm-sh/nvm) (Mac, Linux, Windows via WSL) or [nvm-windows](https://github.com/coreybutler/nvm-windows) (Windows)
- (Optional) [Docker](https://docs.docker.com/get-docker/)

## Setup

The main application uses Django for the backend and Svelte for the frontend.

### Docker

There are two `Dockerfile`s for this project - one for the Django backend and another for the Svelte frontend. These are managed with Docker Compose, and there are two services: `backend` and `frontend`. They can be used as follows:

- Run both development containers: `docker-compose --profile dev up`
- Run just backend: `docker-compose up backend`
- Run just frontend: `docker-compose up frontend`

When the backend container is running, the Django application will run at [http://localhost:8000](http://localhost:8000), along with live-reloading when Python source files change. When the frontend container is running, Rollup will watch the frontend source files for changes and recompile them as necessary.

**NOTE**:

- If you modify `requirements.txt`, you need to do `docker-compose up --build backend` to rebuild the container.
- Any files generated by the Docker containers will be owned by root. To avoid this issue:
  - On Mac/Linux, find your UID using `id -u` and GID using `id -g`. On Windows, you can use 1000 for both UID and GID.
  - Add a `.env` file containing the following:
    ```bash
    UGID=1000:1000
    ```
    Replace the first "1000" with your UID and the second "1000" with your GID.

### Manual

#### Backend

A Python virtual environment can be used to manage backend dependencies:

- Create a virtual environment called `.venv` using: `python3 -m venv .venv`
- Activate this virtual environment; the command depends on which shell is being used:
  - `bash`: `source ./.venv/bin/activate`
  - `cmd`: `.\.venv\Scripts\Activate.bat`
  - PowerShell: `.\venv\Scripts\Activate.ps1`
- Install the dependencies from `requirements.txt`: `pip3 install -r requirements.txt`
- Create database migrations using `python manage.py makemigrations backend_api`
- Perform database migrations using `python manage.py migrate`

#### Frontend

Frontend dependencies are managed using NodeJS. First, run `npm install` to download the required dependencies. Then, these scripts (when run in the `frontend` directory) can be used to manage the frontend:

```bash
npm run build   # Compiles the Svelte app in production mode, placing the output in 'frontend/public/build'
                # This must be done before deploying the application
npm run dev     # Compiles the Svelte app in development and watches for any changes that need to be recompiled
```

For development, Django has been configured to host the files from `frontend/public`, as this folder will contain the final build output.

## OpenAPI Schema

The backend API provides an OpenAPI schema that can be generated using `drf_spectacular`. The auto-generated code is in TypeScript (to make development easier), but this is compiled down to JavaScript and can be consumed as normal.

### With Docker

Two `cli-only` services are configured with Docker Compose. They can be run by doing:

```bash
docker-compose --profile cli-only up
```

This will update the file under [`openapi_schema/schema.yml`](./openapi_schema/schema.yml), and will generate the TypeScript API client code in `frontend/kumon_app_backend_api`.

### Manually

First, install the [OpenAPI Generator CLI](https://openapi-generator.tech/docs/installation) using one of the methods they list.

Then, generate the schema file by running:

```bash
python manage.py spectacular --file openapi_schema/schema.yml
```

Finally, generate the TypeScript API client code using (**NOTE**: TypeScript is used for IntelliSense):

```bash
openapi-generator-cli generate -i openapi_schema/schema.yml -c openapi_schema/generator_config.json -g typescript-fetch -o frontend/kumon_app_backend_api
```

### Issues with `ImportApi.ts`

OpenAPI Generator creates incorrect code for `ImportApi.ts`, as the `type` enum is not used correctly. See these GitHub issues for more context:

- [Enums being treated as complex objects instead of strings](https://github.com/OpenAPITools/openapi-generator/issues/10729)

Any changes to the import API client are currently ignored - if you really need to change something there, comment out this line in [`frontend/kumon_app_backend_api/.openapi-generator-ignore`](./frontend/kumon_app_backend_api/.openapi-generator-ignore):

```sh
src/apis/ImportApi.ts
```

After you've made your changes and have run the generator, make the following changes to [`frontend/kumon_app_backend_api/src/apis/ImportApi.ts`](./frontend/kumon_app_backend_api/src/apis/ImportApi.ts):

- Add these two imports to the top of the file:
  ```diff
  import {
  +   ModelFile,
  +   ModelFileFromJSON,
      TypeEnum,
      TypeEnumFromJSON,
      TypeEnumToJSON,
  } from '../models';
  ```
- Change these two function signatures:
  ```diff
  -   async importListRaw(initOverrides?: RequestInit): Promise<runtime.ApiResponse<Array<any>>> {
  +   async importListRaw(initOverrides?: RequestInit): Promise<runtime.ApiResponse<Array<ModelFile>>> {
  ...
  -   async importList(initOverrides?: RequestInit): Promise<Array<any>> {
  +   async importList(initOverrides?: RequestInit): Promise<Array<ModelFile>> {
  ```
- Modify this line of code in `importCreateRaw`:
  ```diff
  -   formParams.append('type', new Blob([JSON.stringify(TypeEnumToJSON(requestParameters.type))], { type: "application/json", }));
  +   formParams.append('type', requestParameters.type as any);
  ```
- Modify this line of code in `importListRaw`:
  ```diff
  -   return new runtime.JSONApiResponse<any>(response);
  +   return new runtime.JSONApiResponse(response, (jsonValue) => jsonValue.map(ModelFileFromJSON));
  ```

Finally, either re-run the frontend docker container or run `npm install` so that these changes are properly reflected.

## Usage

The final application will be distributed as a desktop app. This is achieved through a custom wrapper script that runs the Django app and a web browser simultaneously. The concept was taken from [`flaskwebgui`](https://github.com/ClimenteA/flaskwebgui), which could not be used as the WSGI server did not terminate after the browser was closed.

For development, use either of these commands to run the application:

- "Wrapped" Desktop App: `python gui.py`
- Web Server Only: `python manage.py runserver`

To package the app for distribution:

  - Run `python build.py`. This will generate a bundle in the `dist` directory.

## Dummy Data Generator

To create and load dummy data into the database navigate to `backend_api/data_gen` and run the following command: `python loaddata.py`.

You can add the following extensions to it:
 - `--password <input-password>` - to manually set the password of the admin account
 - `--save-passwords` - to save the username and passwords of all staff accounts to a .csv file
