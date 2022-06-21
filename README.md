# Test AMCEF

**Test task for the company AMCEF**
Developed by **Nosov Vladyslav**
API for working with posts in the database and working with third-party APIs.


## Requirements

- Python 3.7+
- Django 4.0+

## Tools used for writing API

- ORM
- GIT
- REST
- Error processing
- Working with third party APIs 
(https://jsonplaceholder.typicode.com/)

## Installation

### Virtual environment

Сreating a virtual environment
(in the console)
```
python -m venv env
```

Activating a virtual environment in the console
(for Linux)
```
source env/Scripts/activate
```
(for Windows)
```
env/Scripts/activate
```

Deactivating
```
deactivate
```

### Installing Libraries
```
cd amcef
pip install -r requirements.txt
```
### Project start
Migrations
```
cd amcef
python manage.py makemigrations
python manage.py migrate
```
Launch of the project
```
python manage.py runserver
```



## Functional

### Getting all posts
Method **GET**
```
../api/posts
```
### Getting posts by id or userId
Method **GET**
```
../api/posts?id=8?userid=9
```
### Create new post
Method **POST**
```
../api/posts
```
Request body
```
{
    "userId": 1,
    "title": "char",
    "body": "char"
}
```
### Update post by ID
Method **PUT**
```
../api/posts/{id}
```
Request body
```
{
    "userId": 1,
    "title": "char",
    "body": "char"
}
```
### Delete post by ID
Method **DELETE**
```
../api/posts/{id}
```
