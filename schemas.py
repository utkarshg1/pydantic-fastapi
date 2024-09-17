from pydantic import BaseModel, EmailStr


# Pydantic model for user input and validation
class UserCreate(BaseModel):
    name: str
    email: EmailStr


# Update user
class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None


# Pydantic model for user response
class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
