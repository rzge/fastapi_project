from fastapi import APIRouter, HTTPException, status, Response, Depends

from app.exceptions import UserAlreadyExistsException, IncorrectEmailOrPasswordException
from app.users.auth import get_password_hash, verify_password, authenticate_user, create_access_token
from app.users.dao import UsersDAO
from app.users.dependecies import get_current_user
from app.users.models import Users
from app.users.schemas import SUserAuth

router = APIRouter(
    prefix='/auth',
    tags=["Auth & Пользователи"]
)


@router.post("/register")
async def register_user(user_data: SUserAuth):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)  # проверяет наличие юзера в БД
    if existing_user:  # не даём регистрироваться, если уже есть почта
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException
    # если пользователь есть, создаём jwt токен и отправляем в куки
    access_token = create_access_token({"sub": str(user.id)})  # в jwt токене ключ должен приводиться к строке
    # засетим куку в ответе
    response.set_cookie("booking_access_token", access_token,
                        httponly=True)  # httponly чтоб не перехватывал джаваскрипт
    return {"access_token": access_token}


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("booking_access_token")


@router.get("/me")
async def read_user_me(current_user: Users = Depends(get_current_user)):
    return current_user

