## Introduction
This is a simple Django web application that provides a REST API to retrieve location information based on a ZIP code. It uses the [ZipCodeAPI](https://www.zipcodeapi.com/) to get the location information.

## Features
- Django API implementation.
- API to request information about certain ZIP code.
- Dependency injection from urls.py into views.py.
- SQLite database to save the information when it's new and retrive it when it already exists.
- Call to an external API using an API KEY, only when the ZIP code does not exists in the database.
- JWT authentication with token retrival and refresh endpoint.
- Logging.

## Prerequisites
- Python 3.6 or higher
- Django 3.2 or higher
- Requests library
- Django REST framework
- Django REST Framework Simple JWT

## Installation
1. Clone this repository: `git clone https://github.com/Huakus/pythonTestProject.git`.
2. Navigate into the project directory: `cd pythonTestProject`.
3. Create a virtual environment: `python3 -m venv env`.
4. Activate the virtual environment: `source env/bin/activate`.
5. Set the `ZIPCODE_API_KEY` environment variable with your ZipCodeAPI key: `export ZIPCODE_API_KEY=<your-key>`.
6. Migrate the database: `python manage.py migrate`.
7. Run the development server: `python manage.py runserver`.

## Usage
To retrieve the location information based on a ZIP code, send a GET request to `/location/<str:zip_code>/`. You must include a valid JWT token in the Authorization header.

The API returns a JSON object with the following fields:

- `zip_code`: the ZIP code used to retrieve the location information
- `name`: the city name
- `lat`: the latitude
- `lon`: the longitude
- `state`: the state name

If the location information for the given ZIP code is not in the database, the API will retrieve it from the ZipCodeAPI and store it in the database before returning it.

## Code Structure
- `pythonTestProject/urls.py`: defines the application's URL routing.
- `zipcodes/views.py`: defines the views that handle the API requests.
- `zipcodes/models.py`: defines the Location model.
- `zipcodes/services.py`: defines the service layer that interacts with the ZipCodeAPI and stores/retrieves Location objects from the database.
- `zipcodes/serializers.py`: defines the serializer for the Location model.

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
