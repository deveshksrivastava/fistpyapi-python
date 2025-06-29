# Python

## start fastAPI

 - pip install fastapi
 - pip install fastapi[all] ths will install every thing including uvicorn
 - pip install "uvicorn[standard]" - helps to run the fast api like 
 - pip install python-multipart sqlalchemy jinja2
 - python -m uvicorn app:app --reload
 - python -m uvicorn main:app --reload

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

