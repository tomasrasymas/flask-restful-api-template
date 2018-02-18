# Flask-RESTful API project template

This project shows one of the possible ways to implement RESTful API server.

There are implemented two models: User and Todo, one user has many todos.

Main libraries used:
1. Flask-Migrate - for handling all database migrations.
2. Flask-RESTful - restful API library.
3. Flask-Script - provides support for writing external scripts.
4. Flask-SQLAlchemy - adds support for SQLAlchemy ORM.

Project structure:
```
.
├── README.md
├── app.py
├── endpoints
│   ├── __init__.py
│   ├── todos
│   │   ├── __init__.py
│   │   ├── model.py
│   │   └── resource.py
│   └── users
│       ├── __init__.py
│       ├── model.py
│       └── resource.py
├── manage.py
├── requirements.txt
└── settings.py
```

* endpoints - holds all endpoints.
* app.py - flask application initialization.
* settings.py - all global app settings.
* manage.py - script for managing application (migrations, server execution, etc.)

## Running 

1. Clone repository.
2. pip install requirements.txt
3. Run following commands:
    1. python manage.py db init
    2. python manage.py db migrate
    3. python manage.py db upgrade
4. Start server by running python manage.py runserver

## Usage
### Users endpoint
POST http://127.0.0.1:5000/api/users

REQUEST
```json
{
	"name": "John John"
}
```
RESPONSE
```json
{
    "id": 1,
    "name": "John John",
    "todos": []
}
```
PUT http://127.0.0.1:5000/api/users/1

REQUEST
```json
{
	"name": "Smith Smith"
}
```
RESPONSE
```json
{
    "id": 1,
    "name": "Smith Smith",
    "todos": []
}
```
DELETE http://127.0.0.1:5000/api/users/1

RESPONSE
```json
{
    "id": 3,
    "name": "Tom Tom",
    "todos": []
}
```
GET http://127.0.0.1:5000/api/users

RESPONSE
```json
{
    "count": 2,
    "users": [
        {
            "id": 1,
            "name": "John John",
            "todos": [
                {
                    "id": 1,
                    "name": "First task",
                    "description": "First task description"
                },
                {
                    "id": 2,
                    "name": "Second task",
                    "description": "Second task description"
                }
            ]
        },
        {
            "id": 2,
            "name": "Smith Smith",
            "todos": []
        }
    ]
}
```
GET http://127.0.0.1:5000/api/users/2
```json
{
    "id": 2,
    "name": "Smith Smith",
    "todos": []
}
```
GET http://127.0.0.1:5000/api/users?name=John John
```json
{
    "count": 1,
    "users": [
        {
            "id": 1,
            "name": "John John",
            "todos": [
                {
                    "id": 1,
                    "name": "First task",
                    "description": "First task description"
                },
                {
                    "id": 2,
                    "name": "Second task",
                    "description": "Second task description"
                }
            ]
        }
    ]
}
```
GET http://127.0.0.1:5000/api/users?limit=1&offset=1
```json
{
    "count": 1,
    "users": [
        {
            "id": 2,
            "name": "Smith Smith",
            "todos": []
        }
    ]
}
```

Todo endpoint is similar to Users endpoint.