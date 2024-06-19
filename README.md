# Messaging System API

## Description
This project is a backend API developed with Python using Django and Django REST Framework, using PostgreSQL for the database. It provides functionality for users to send, receive, and manage messages within a messaging system.

## Table of Contents
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Structure](#structure)
- [API Documentation](#api-documentation)
- [References and Authors](#references-and-authors)
- [License](#license)

## Setup and Installation
### Prerequisites
- Python 3.x installed on your system.
- Pip package manager.
- PostgreSQL installed and running (optional)

### Installation Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/hadas8/messaging-system
   cd messaging-system-api
2. **Create and activate a virtual environment**
   ```bash 
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
4. **Set up the .env file**
  - Create a .env file in the root directory of your project.
  - Add sensitive settings such as SECRET_KEY and DEBUG in the .env file:
    ```bash
    SECRET_KEY=your_secret_key_here
    DEBUG=True  # Set to False in production

    # PostgreSQL settings (optional):
    # if you're using PostgreSQL, make sure to modify the DATABASES setting in settings.py and use the code commented out
    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=your_db_host
    DB_PORT=your_db_port

5. **Apply database migrations**
    ```bash
    python manage.py migrate
6. **Create a superuser for admin access**
    ```bash
    python manage.py createsuperuser
7. **Run the development server**
    ```bash
    Run the development server

## Usage
- The primary usage of the API includes:
  - User authentication
  - Create and send messages
  - View sent messages
  - View received messages 
  - View unread messages
  - Read a specific message
  - Delete messages
- Access the admin interface at http://localhost:8000/admin/ to manage users, messages, and user message statuses.

## Structure
```
messagingsystem/
│
├── manage.py
├── messagingsystem/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── messaging/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│ └── migrations/
│ └── init.py
├── documentaion.json
└── requirements.txt
```

In this structure:

- **messagingsystem/**: Root directory containing the main Django project files.
  - **manage.py**: Django's command-line utility for administrative tasks.
  - **messagingsystem/**: Django project directory.
    - **__init__.py**: Python package initialization file.
    - **asgi.py**: ASGI config for deploying as an asynchronous web application.
    - **settings.py**: Django project settings and configurations.
    - **urls.py**: URL declarations for the project.
    - **wsgi.py**: WSGI config for deploying as a traditional web application.
- **messaging/**: Django app directory for messaging functionality.
  - **__init__.py**: Python package initialization file.
  - **admin.py**: Django admin configurations for the app.
  - **apps.py**: Django app configuration.
  - **models.py**: Django models defining database structure (Message, UserMessageStatus).
  - **serializers.py**: Django REST Framework serializers for API data serialization.
  - **views.py**: Django views defining API endpoints (MessageCreateView, SentMessagesListView, etc.).
  - **urls.py**: URL declarations for the app's API endpoints.
  - **migrations/**: Directory containing database migrations.

- **requirements.txt**: File listing Python dependencies required for the project.

This structure gives an overview of how the project is organized, including the main project directory, app directory, and key files within each. Adjust the names and specific details to match your actual project structure if necessary.

### Models
- **Message**: Represents a message with fields for sender, receiver, subject, message and creation date.
- **UserMessageStatus**: Tracks read and deleted statuses of messages for each user.

### Serializers
- **MessageSerializer**: Serializes Message objects for API representation.
- **UserMessageStatusSerializer**: Serializes UserMessageStatus objects for API representation.

### Views
- **MessageCreateView**: Creates and sends messages.
- **SentMessagesListView**: Lists sent messages for the authenticated user.
- **ReceivedMessagesListView**: Lists received messages for the authenticated user.
- **UnreadMessagesListView**: Lists unread messages for the authenticated user.
- **MessageDetailView**: Retrieves or deletes a specific message and marks it as read when accessed.

### URLs
- Endpoint URLs are defined in `urls.py` for message creation, message lists, message details, and message deletion.

## API Documentation
- Explore the API documentation using the Swagger documentation file documentation.json
- It can be easily viewd in any online Swagger editor such as: https://editor.swagger.io/

## References and Authors
- Developed by Hadas Etzion
- Third-party tools used: Django, Django REST Framework, PostgreSQL, Python-Decouple

## License
This project is licensed under the MIT License.
