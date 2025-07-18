from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import app.models as models, app.schemas as schemas, app.database as database
import httpx

models.Base.metadata.create_all(bind=models.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_user():
    async with httpx.AsyncClient() as client:
        # response = await client.get(f"http://user_service:8000/users/")
        response = await client.get(f"https://jsonplaceholder.typicode.com/todos/1")
        return response.json()

@app.post("/tasks/")
async def get_users():
    s = await get_user()
    return {"data": s}

@app.get("/")
def read_root():
    return {"message": "Hello from root!"}