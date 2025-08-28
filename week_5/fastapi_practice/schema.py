from pydantic import BaseModel, EmailStr

# ------------------------
# Pydantic Model
# ------------------------
class Item(BaseModel):
    id: str
    name: str


class SignIn(BaseModel):
    username: str
    password: str

class SignUp(BaseModel):
    username: str
    password: str
    email: EmailStr
    id: str

class UserInfo(BaseModel):
    id: str
    username: str
    email: EmailStr