from fastapi import FastAPI, Depends, Request, Form, status
from typing import Annotated
from sqlalchemy.orm import Session

from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
import sqlite3

import models
from database import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")

app = FastAPI()


def show_all_tables(db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for table in tables:
        print(table[0])

    conn.close()

show_all_tables('your_database.db')

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db #yield - code stop before the yield statement and the generator is paused
    finally:
        db.close()

# @app.get("/")
# async def read_all(db: Annotated[Session, Depends=(get_db)]): #Depends - dependency injection, need to do some thing before code exec
#     return db.query(Todos).all()

@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    todos = db.query(models.Todo).all()
    return templates.TemplateResponse("base.html",
                                      {"request": request, "todo_list": todos})

@app.post("/add")
def add(request: Request, title: str = Form(...), db: Session = Depends(get_db)):
    new_todo = models.Todo(title=title)
    db.add(new_todo)
    db.commit()

    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)


@app.get("/update/{todo_id}")
def update(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    todo.complete = not todo.complete
    db.commit()

    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)


@app.get("/delete/{todo_id}")
def delete(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    db.delete(todo)
    db.commit()

    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)