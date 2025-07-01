from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_users_v2():
    return {"version": "v2", "users": ["Alice", "Bob", "Charlie"]}