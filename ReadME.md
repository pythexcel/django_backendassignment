# BackendAssignment - Django Project


## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Running the Development Server](#running-the-development-server)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)

## Introduction
BackendAssignment is a Django project that provides a backend system for managing user registration, authentication, posting content, and user profiles. It is built using Django and Django Rest Framework.

## Features
- User registration and authentication with JWT tokens
- User profile pages with user details, posts, followers, and following
- Posting new content
- PostgreSQL database integration

## Technologies Used
- Django
- Django Rest Framework
- PostgreSQL (as the database)
- Other relevant technologies...

## Getting Started
Follow these steps to set up and run the project on your local machine.

### Installation
1. Clone this repository to your local machine:

2. Change into the project directory:

3. Create a virtual environment (recommended):

4. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

5. Install project dependencies:
  - pip install -r requirements.txt

### Configuration
1. Configure your database settings in `BackendAssignment/settings.py`. By default, the project is set to use PostgreSQL. Update the database settings to match your local configuration.

2. Create a `.env` file in the project directory and add the following environment variables:

 - DATABASE_NAME=<your_database_name>
 - DATABASE_USER=<your_user_name>
 - DATABASE_PASSWORD=<your_database_password>
 - DATABASE_HOST=<database_host>
 - DATABASE_PORT=<datbase_port>

3. Migrate the database to create the necessary tables:
  - python manage.py makemigrations
  - python manage.py migrate


### Running the Development Server
Start the development server by running the following command:
 - python manage.py runserver


The server will start at `http://localhost:8000/`.

## API Endpoints
- `/api/user/register/`: Register a new user.
- `/api/user/login/`: Authenticate and obtain a JWT token.
- `/api/user/profile/`: Retrieve or update the user's profile.
- `/api/user/follow/<user_id>/`: Follow another user.
- `/api/user/unfollow/<user_id>/`: Unfollow another user.
- `/api/posts/`: List and create posts.
- `/api/posts/<post_id>/`: Retrieve, update, or delete a specific post.

[Add more endpoints and descriptions as needed]

## Authentication
To access protected endpoints, you need to include the JWT token in the `Authorization` header of your requests. The token can be obtained by logging in using the `/api/user/login/` endpoint.

Example:
  Authorization: Bearer your-jwt-token