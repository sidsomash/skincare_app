from pydantic import BaseModel, Field, EmailStr, field_validator
import re

class RegistrationRequest(BaseModel):
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

class LoginRequest(BaseModel):
    username: str
    password: str
