# Django Task Management Project

This is a Django-based task management project that allows users to create, update, fetch, and delete tasks. The project also includes API endpoints to fetch tasks based on their status (In Progress, Completed, Overdue).

## Features

- User authentication and authorization using JWT (JSON Web Tokens)
- Task management (CRUD operations)
- API endpoints to fetch tasks based on their status
- Unit tests for views and models
- Django templates for displaying tasks

## Prerequisites

- Python 3.8 or higher
- Django 3.2 or higher
- Django REST framework
- Django REST framework Simple JWT

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the application:**

    Open your web browser and navigate to `http://localhost:8000/`.

## API Endpoints

The project includes the following API endpoints:

- Fetch tasks by status:
