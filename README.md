# Messaging System API

## Description
This project is a backend API developed with Python using Django and Django REST Framework. It provides functionality for users to send, receive, and manage messages within a messaging system.

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
- Virtual environment tool (venv) for Python.

### Installation Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/hadas8/messaging-system.git
   cd messaging-system-api
2. **Create and activate a virtual environment**
   ```bash 
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
4. **Apply database migrations**
    ```bash
    python manage.py migrate
5. **Create a superuser for admin access**
    ```bash
    python manage.py createsuperuser
6. **Run the development server**
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
- Explore the API documentation using Swagger UI available at [http://localhost:8000/swagger/](http://localhost:8000/swagger/).

## References and Authors
- Developed by Hadas Etion
- Third-party tools used: Django, Django REST Framework

## License
This project is licensed under the MIT License.
