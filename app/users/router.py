from fastapi import APIRouter, HTTPException, status, Response

from app.users.auth import get_password_hash, verify_password, authenticate_user, create_access_token
from app.users.dao import UsersDAO
from app.users.schemas import SUserAuth

router = APIRouter(
    prefix='/auth',
    tags=["Auth & Пользователи"]
)


@router.post("/register")
async def register_user(user_data: SUserAuth):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)  # проверяет наличие юзера в БД
    if existing_user:  # не даём регистрироваться, если уже есть почта
        raise HTTPException(status_code=500)
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    # если пользователь есть, создаём jwt токен и отправляем в куки
    access_token = create_access_token({"sub": user.id})
    # засетим куку в ответе
    response.set_cookie("booking_access_token", access_token, httponly=True) # httponly чтоб не перехватывал джаваскрипт
    return access_token