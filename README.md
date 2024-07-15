# Theater Ticketing System

The Theater Ticketing System is a web application that allows administrators to manage theaters and their seating arrangements, while users can view and reserve seats for specific dates and shows. The system is built using Django and utilizes PostgreSQL as the database. Redis is used for caching, and Celery with Redis is used for task queue and scheduling. JWT (JSON Web Tokens) is used for authentication.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.8+
- Django
- PostgreSQL
- pipenv

## Project Setup

### 1. Clone the Repository

Clone this repository to your local machine using the following command:

```sh
git https://github.com/bochiedev/theater_ticketing.git
cd theater_ticketing
```

### 2. Set Up the Environment

Navigate to the project directory and set up a virtual environment using pipenv:

```sh
pipenv install --dev
pipenv shell
```

### 3. Install Project Dependencies

Install the necessary dependencies:

```sh
pipenv install django psycopg2-binary djangorestframework djangorestframework-simplejwt celery redis
```

### 4. Set Up PostgreSQL Database

Ensure you have PostgreSQL installed and running on your machine. Create a new PostgreSQL database:

```sql
CREATE DATABASE theater_ticketing;
CREATE USER yourusername WITH PASSWORD 'yourpassword';
ALTER ROLE yourusername SET client_encoding TO 'utf8';
ALTER ROLE yourusername SET default_transaction_isolation TO 'read committed';
ALTER ROLE yourusername SET timezone TO 'UTC+3';
GRANT ALL PRIVILEGES ON DATABASE theater_ticketing TO yourusername;
```

### 5. Configure Database Settings

Update your Django project settings to connect to the PostgreSQL database. Open `theater_ticketing/settings.py` and update the `DATABASES` section:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'theater_ticketing',
        'USER': 'yourusername',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

### 6. Run Migrations

Apply the database migrations to set up the initial database schema:

```sh
python manage.py migrate
```

### 7. Create a Superuser

Create a superuser account to access the Django admin interface:

```sh
python manage.py createsuperuser
```

### 8. Run the Development Server

Start the Django development server:

```sh
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/`.

## Additional Setup

### Redis and Celery Setup

To use Redis as the message broker for Celery, make sure Redis is installed and running. Update your Django project settings to configure Celery. Open `theater_ticketing/settings.py` and add the following:

```python
# Celery Configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
```

Start the Celery worker in a new terminal window:

```sh
celery -A theater_ticketing worker --loglevel=info
```

### JWT Authentication

The project uses JWT for authentication. To log in and obtain a JWT token, send a POST request to `/api/token/` with your username and password. Use this token to authenticate subsequent requests by including it in the Authorization header with the prefix JWT:

```http
Authorization: JWT <your_jwt_token>
```

## Project Structure

The project directory structure is as follows:

```
theater_ticketing/
│
├── manage.py
├── theater_ticketing/
│   ├── __init__.py
│   ├── .env
│   ├── env.example
│   ├── celery.py
│   ├── settings.py
│   ├── managers.py
│   ├── serializers.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── users/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   ├── tests.py
│   ├── tasks.py
│   └── utils.py
├── theaters/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   ├── tests.py
│   ├── tasks.py
│   └── utils.py
└── reservations/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── urls.py
    ├── views.py
    ├── tests.py
    ├── tasks.py
    └── utils.py
```

## API Endpoints

### User Authentication

#### Register a New User

- **URL:** `/api/v1/auth/users/`
- **Method:** `POST`
- **Request Body:**

  ```json
  {
    "email": "user@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "password": "password123"
  }
  ```

- **Response:**

  ```json
  {
    "uid": "5f8a5312-d168-4b7e-bf42-fd1839330a36",
    "email": "user@example.com",
    "first_name": "John",
    "last_name": "Doe"
  }
  ```

#### Login to Obtain a JWT Token

- **URL:** `/api/v1/auth/token/`
- **Method:** `POST`
- **Request Body:**

  ```json
  {
    "email": "user@example.com",
    "password": "password123"
  }
  ```

- **Response:**

  ```json
  {
    "refresh": "your-refresh-token",
    "access": "your-access-token"
  }
  ```

### Admin Management

#### Create a New Theater

- **URL:** `/api/v1/theater/`
- **Method:** `POST`
- **Request Body:**

  ```json
  {
    "name": "Main Theater",
    "total_seats": 100
  }
  ```

- **Response:**

  ```json
  {
    "uid": "5f8a5312-d168-4b7e-bf42-fd1839330a36",
    "name": "Main Theater",
    "total_seats": 100
  }
  ```

#### Create Seating for a Specific Date

- **URL:** `/api/v1/seating/`
- **Method:** `POST`
- **Request Body:**

  ```json
  {
    "theater": "5f8a5312-d168-4b7e-bf42-fd1839330a36",
    "title": "Mad Max 4",
    "date": "2024-07-15"
  }
  ```

- **Response:**

  ```json
  {
    "uid": "5f8a5312-d168-4b7e-bf42-fd1839330a36",
    "title": "Mad Max 4",
    "theater": "5f8a5312-d168-4b7e-bf42-fd1839330a36",
    "date": "2024-07-15"
  }
  ```

### User Interaction

#### List All Theaters Available for Specific Dates

- **URL:** `/api/v1/theater/`
- **Method:** `GET`
- **Response:**

  ```json
  [
    {
      "uid": "5f8a5312-d168-4b7e-bf42-fd1839330a36",
      "name": "Main Theater",
      "total_seats": 100,
      "seatings": [
        {
          "uid": "5f8a5312-d168-4b7e-bf42-fd1839330a36",
          "date": "2024-07-15"
        }
      ]
    }
  ]
  ```

#### List Available Seats for a Selected Theater

- **URL:** `/api/v1/seating/{uid}/`
- **Method:** `GET`
- **Response:**

  ```json
  {
    "uid": "5f8a5312-d168-4b7e-bf42-fd1839330a36",
    "theater": "5f8a5312-d168-4b7e-bf42-fd1839330a36",
    "date": "2024-07-15",
    "available_seats": [1, 2, 3, ..., 100],
    "booked_seats": [10, 15, 20]
  }
  ```

#### Reserve a Preferred Seat for a Specific Show

- **URL:** `/api/v1/reservation/`
- **Method:** `POST`
- **Request Body:**

  ```json
  {
    "seating": "5f8a5312-d168-4b7e-bf42-fd1839330a36",
    "seat_number": 25
  }
  ```

- **Response:**

  ```json
  {
    "uid": "5f8a5312-d168-4b7e-bf42-fd1839330a36",
    "user": 1,
    "seating": 1,
    "seat_number": 25
  }
  ```

## Running Tests

To run the tests for the project, use the following command:

```sh
python manage.py test
```
