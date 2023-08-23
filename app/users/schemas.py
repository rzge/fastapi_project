from pydantic import BaseModel, EmailStr


class SUserRegister(BaseModel):
    email: EmailStr  # валидирует почту
    password: str
