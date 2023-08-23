from pydantic import BaseModel, EmailStr


class SUserAuth(BaseModel):
    email: EmailStr  # валидирует почту
    password: str
