# Todo App

A robust Django-based Todo application featuring user authentication, profile picture management, and seamless Docker deployment. The application is thoroughly tested using Django's `TestCase` and `pytest` to ensure reliability across various scenarios.

## Features

- Secure user authentication (login, logout, registration and Delete )
- Create, update, and delete tasks effortlessly
- User profiles with the ability to upload and manage profile pictures
- Comprehensive test coverage using Django's `TestCase` and `pytest`
- Dockerized setup for simplified deployment

## Installation

### 1. Clone the Repository

```sh
https://github.com/AmirScheldon/ToDo.git
cd ToDo
```

### 2. Set Up Virtual Environment (Optional)

```sh
python -m venv .env
source .env/bin/activate  # On Windows use: .env\Scripts\activate
```

### 3. Install Dependencies

Using Pipenv:

```sh
pip install pipenv
pipenv install --dev
```

### 4. Apply Migrations

```sh
python manage.py migrate
```

### 5. Create a Superuser

```sh
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 6. Run the Development Server

```sh
python manage.py runserver
```

## Running Tests

### Using Django TestCase

```sh
python manage.py test
```

### Using Pytest

```sh
pytest
```

## Docker Deployment

### 1. Build and Run with Docker Compose

```sh
docker-compose up --build
```

### 2. Stop the Containers

```sh
docker-compose down
```

This will build and start the application along with any necessary services, such as a database, based on the `docker-compose.yml` configuration.

### 1. Build the Docker Image

```sh
docker build -t todo-app .
```

### 2. Run the Container

```sh
docker run -p 8000:8000 todo-app
```

## API Endpoints

All API endpoints are designed with security in mind, ensuring safe and efficient operations.

| Method | Endpoint                   | Description         |
| ------ | -------------------------- | ------------------- |
| GET    | `/home/`                   | Home page           |
| GET    | `/tasks/`                  | List all tasks      |
| POST   | `/create-task/`            | Create a new task   |
| PUT    | `/update-task/<int:pk>`    | Update a task       |
| DELETE | `/delete-task/<int:pk>`    | Delete a task       |
| GET    | `/profile`                 | View user profile   |
| PUT    | `/profile/update`          | Update user profile |
| DELETE | `/profile/delete/<int:pk>` | Delete user profile |
| GET    | `/`                        | First page          |
| POST   | `/auth/register/`          | User registration   |
| POST   | `/auth/login/`             | User login          |
| POST   | `/auth/logout/`            | User logout         |

