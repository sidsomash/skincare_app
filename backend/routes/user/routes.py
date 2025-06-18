from fastapi import APIRouter, HTTPException, status
from models.user.schemas import RegistrationRequest, LoginRequest
from auth import hash_password, verify_password, create_access_token

router = APIRouter()
users = {}  # In-memory storage


@router.post("/user/create")
def create_user(user: RegistrationRequest):
    if user.username in users:
        raise HTTPException(status_code=400, detail="Username already exists")

    users[user.username] = {
        "email": user.email,
        "hashed_password": hash_password(user.password)
    }
    return {"message": "User created successfully"}


@router.post("/user/login")
def login(creds: LoginRequest):
    user = users.get(creds.username)
    if not user or not verify_password(creds.password, user["hashed_password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = create_access_token(data={"sub": creds.username})
    return {"access_token": token, "token_type": "bearer"}
