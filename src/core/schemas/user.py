from pydantic import BaseModel

class CreateUser(BaseModel):
    id_role: int = 1
    name: str
    surname: str
    patronymic: str
    password: str
    email: str
    is_active: bool = True

class User(BaseModel):
    id: int
    id_role: int
    name: str
    surname: str
    patronymic: str
    password: str
    email: str
    is_active: bool