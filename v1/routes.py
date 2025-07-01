from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_users_v1():
    return {"version": "v1", "users": ["Alice", "Bob"]}