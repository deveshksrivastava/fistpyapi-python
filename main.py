from fastapi import FastAPI, HTTPException, Depends, Request, Form, status
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# Create an instance of the FastAPI class
app = FastAPI()

items = []
# Define a route using a decorator and async function
@app.get("/")  # Decorator for GET requests to the root URL
async def read_root():
    return {"message": "Hello, World!"}

# $ curl -X GET 'http://127.0.0.1:8000/items?limit=2'
@app.get("/items")
def list_items(limit: int = 10):
    # return items
    return items[0:limit]

# curl -X GET http://127.0.0.1:8000/items/2 
# Get an Item by ID : items/2 
@app.get("/items/{item_id}")  # Decorator for GET requests with path parameter
async def get_item(item_id: int):  # Path parameter with type integer
    if item_id >= len(items):
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    item = items[item_id]
    return item #return {"item_id": item_id}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


# curl -X POST -H "Content-Type: application/json" "http://127.0.0.1:8000/items?item=apple"
@app.post("/items")
def create_item(item: str):
    print("Received item:", item)
    items.append(item)
    return items


@app.post("/itemsMx/")
async def create_itemMx(item: Item):
  item_dict = item.dict() #dictionary 
  if item.tax:
    price_with_tax  = item.price + item.tax
    item_dict.update({"price_with_tax":price_with_tax})
  return item_dict

#declare path parameters and a request body at the same time
@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}