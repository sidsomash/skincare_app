from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel, Field, EmailStr, validator, field_validator
import re

app = FastAPI()

class User(BaseModel):
    username: str = Field(min_length=8, max_length=20)
    email: EmailStr
    password: str = Field(min_length=8, max_length=20)

    @field_validator("password")
    def validate_password(cls, value):
        """Ensure password contains at least one uppercase, one number, and one special character."""
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter.")
        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one number.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError("Password must contain at least one special character.")
        return value

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/user/create")
async def create_user(user: User):
    return user

