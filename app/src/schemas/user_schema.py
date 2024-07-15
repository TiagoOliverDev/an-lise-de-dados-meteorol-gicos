from pydantic import BaseModel, EmailStr, constr

class LoginData(BaseModel):
    email: EmailStr
    password: str

class UserCreate(BaseModel):
    email: EmailStr
    password: constr(min_length=8)