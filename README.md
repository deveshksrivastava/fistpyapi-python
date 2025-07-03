# Python

# Educational-Purpose
In this Repository I will share fastapi core concepts for my YouTube subscribers
1. What is Path parameters
2. What is Query parameters
3. Choice field in FastAPI
4. What is Request Body
5. Declare request example data
6. Fastapi Validations
7. Fastapi Form data
8. Fastapi File Upload
9. Fastapi Error Handling
10. Fastapi DataBase Connectivity
11. Fastapi Restful API's
12. Fastapi Nested Models
13. Fastapi OAuth2 with password and hashing jwt token
14. Fastapi Role based uthentication
15. Fastapi Unit Testing
# https://github.com/Coding-Crashkurse/FastAPI-Auth/tree/main/fastapi/app  (imp link)

## start fastAPI

 - pip install fastapi
 - pip install fastapi[all] ths will install every thing including uvicorn
 - pip install "uvicorn[standard]" - helps to run the fast api like 
 - pip install python-multipart sqlalchemy jinja2
 - python -m uvicorn app:app --reload
 - python -m uvicorn main:app --reload
 - python -m uvicorn connectdb.maindb:app --reload    : to run from folder, should have __init__py and call from connectdb import 
 maindb from main
 - python -m uvicorn TASK_SERVICE.main:app --reload   -> run inside the task_Service folder there is main.py file

## Working Directory
```
fistpyapi/
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── main.py
├── app/
│   ├── __init__.py
│   ├── core/
│   │   ├── config.py            # Environment config & settings
│   │   └── security.py          # Auth/JWT handling
│   ├── models/
│   │   └── user.py              # SQLAlchemy or Pydantic models
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   └── user_routes.py   # e.g., /v1/users
│   │   └── v2/
│   │       ├── __init__.py
│   │       └── user_routes.py   # e.g., /v2/users
│   ├── services/
│   │   └── user_service.py      # Business logic
│   ├── db/
│   │   ├── base.py
│   │   ├── models.py
│   │   └── session.py           # DB connection setup
│   └── schemas/
│       └── user_schema.py       # Pydantic request/response models
└── tests/
    └── test_users.py
```

## Why fast Api
 - Async by default
 - easy to define route, error handling
 - large communit support
 - easy to use
 - Djngo is hevey weight

# View the application
 - http://127.0.0.1:8000/ (html view)
 - http://127.0.0.1:8000/docs (Swager view)
 - http://127.0.0.1:8000/redoc (diffrent swager view)
 - http://127.0.0.1:8000/openapi.json (Json View)



## Learn Python from UDEMY
 - https://fastapi.tiangolo.com/tutorial/first-steps/ (fast api documents)
 - https://github.com/Pierian-Data/Complete-Python-3-Bootcamp
 - https://www.youtube.com/watch?v=iWS9ogMPOI0
 - https://youtu.be/VFu95RjLSQ8

 - https://github.com/ArjanCodes/2023-fastapi
 - https://www.youtube.com/watch?v=SORiTsvnU28

- use can use the simple rest client or postman to run it.
 - curl -X "POST" "http://127.0.0.1:8000/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"foo\": \"bar\"}"
 - curl -X POST -H "Content-Type: application/json" "http://127.0.0.1:8000/items?item=apple" 
 - curl -X GET http://127.0.0.1:8000/items/2 
 - $ curl -X GET 'http://127.0.0.1:8000/items?limit=2'

## BaseModel
In FastAPI, BaseModel comes from Pydantic and is used for data validation and serialization. It helps define structured data models, ensuring that incoming and outgoing data follows a specific format.
### Key Uses of BaseModel in FastAPI:
 - Automatic Data Validation – Ensures that request data matches the expected types.
 - Serialization & Deserialization – Converts Python objects into JSON and vice versa.
 - Improved API Documentation – FastAPI automatically generates OpenAPI docs based on BaseModel.
 - Default Values & Constraints – Allows setting default values and validation rules
 - Path and Query are used to define and validate parameters in API routes.

## Learn more about - Step by step
 - https://realpython.com/fastapi-python-web-apis/

## HTTP request methods:
  - POST
  - GET
  - PUT
  - DELETE
  - OPTIONS
  - HEAD
  - PATCH
  - TRACE


## You can also use the other operations mentioned above:
@app.post()
@app.put()
@app.delete()
@app.options()
@app.head()
@app.patch()
@app.trace()

difference between normal functions and async functions and when to use them


Data Handling With pydantic : data validation
  -  str, float, bool
-  


Request Body: Receiving JSON Data
  - Use pydantic to Declare JSON Data Models (Data Shapes)
  - import BaseModel from pydantic and then use it to create subclasses defining the schema, or data shapes, you want to receive.
  
  ```
    from typing import Optional
    from pydantic import BaseModel

    class Item(BaseModel):
      name: str
      description: Optional[str] = None
      price: float
      tax: Optional[float] = None  

    @app.post("/items/")
    async def create_item(item: Item):
        return item

  ```
Which Python Framework is best? Django vs Flask vs FastAPI
  https://www.youtube.com/watch?v=3vfum74ggHE
  https://github.com/patrickloeber/python-fun/tree/master/webapps

Udemy
https://tcsglobal.udemy.com/course/fastapi-the-complete-course/learn/lecture/29025832#overview

  ## Request Body and Path Parameters
You can declare path parameters and a request body at the same time.
    ```
    @app.put("/items/{item_id}")
    async def create_item(item_id: int, item: Item):
        return {"item_id": item_id, **item.dict()}
     ```

ORM:
sqlalchemy (pip install sqlalchemy)


Connecting Sql light

D:\sites\LearnPython\fistpyapi>sqlite3
sqlite> .schema
sqlite>  create table todos (id INTEGER NOT NULL, title VARCHAR,desc VARCHAR, PRIMARY KEY (id));
sqlite>  
    insert into todos (id, title, desc)values (1, 'Tero No1', 'Tero No 1 is the title');
    insert into todos (id, title, desc)values (2, 'Tero No2', 'Tero No 2 is the title');
    insert into todos (id, title, desc)values (3, 'Tero No3', 'Tero No 3 is the title');
sqlite>  insert into todos where id=2;
sqlite> select * from todos;
    1|BookDay|THIS IS ABOUT THE HOME PAGE

sqlite> .mode column
sqlite> select * from todos;
id  title    desc
--  -------  ---------------------------
1   BookDay  THIS IS ABOUT THE HOME PAGE


sqlite> .mode markdown
sqlite> select * from todos;
| id  | title   | desc                        |
| --- | ------- | --------------------------- |
| 1   | BookDay | THIS IS ABOUT THE HOME PAGE |


sqlite> .mode box
sqlite> .mode table
sqlite> select * from todos;
┌────┬─────────┬─────────────────────────────┐
│ id │  title  │            desc             │
├────┼─────────┼─────────────────────────────┤
│ 1  │ BookDay │ THIS IS ABOUT THE HOME PAGE │
└────┴─────────┴─────────────────────────────┘


### instal Sqlite
#### To install SQLite3 on Windows 10, follow these steps:
 - Download SQLite Tools Go to the official SQLite download page and look for the section titled "Precompiled Binaries for Windows". Download the file named sqlite-tools-win-x64-*.zip (or win-x86 if you're on 32-bit).
 - Extract the ZIP File Extract the contents to a folder, for example: C:\sqlite. Inside, you’ll find sqlite3.exe, which is the command-line tool.
 - Add SQLite to System Path (Optional but Recommended)
   - Open the Start menu, search for Environment Variables, and click Edit the system environment variables.
   - In the System Properties window, click Environment Variables.
   - Under System variables, find and select Path, then click Edit.
   - Click New and add the path to your SQLite folder (e.g., C:\sqlite).
   - Click OK to close all windows.
 - Verify Installation Open Command Prompt and type: sqlite3
 - pip install fastapi uvicorn sqlalchemy

### Setting up database and models
```
# db.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

```

### Create a Virtual Environment (recommended)
```
1. Run command in terminal
python -m venv venv
venv\Scripts\activate   # For Windows

2. Install Your Packages
pip install fastapi uvicorn sqlalchemy pydantic fastapi-pagination

3. Freeze Installed Packages into requirements.txt
pip freeze > requirements.txt

This creates a requirements.txt like:
fastapi==0.110.0
uvicorn==0.29.0
sqlalchemy==2.0.30
pydantic==2.7.1
fastapi-pagination==0.12.24
(Optional: You can manually edit this file to remove unneeded dependencies.)

4. Installing from requirements.txt Later
To recreate your environment on another machine:
  pip install -r requirements.txt

or 
Option 2: Use a Clean Virtual Environment Sometimes starting fresh helps:

python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt

Update dependency 
python -m pip install --upgrade pip

```

### Logging
```
import logging

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
# logger.info("This is an info message")
# logger.warning("This is a warning")
# logger.error("This is an error")

```


### Docker:
```
# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]



docker build -t my-fastapi-app .
docker run -d -p 8000:8000 my-fastapi-app

```

```
python -m uvicorn main:basic --reload


docker build -t my-fastapi-app .
docker run -d -p 8000:8000 my-fastapi-app


**************
## use command line
python -m venv venv
venv\Scripts\activate  # On Windows
--> add file to requirement.txt
pip install -r requirements.txt

```

### Module not installed
```
python --version
pip --version
If they don’t match, use:

python -m pip install pyodbc
🧪 Step 3: Test the Install
After installing, test it in Python:

python
import pyodbc
print(pyodbc.version)
```