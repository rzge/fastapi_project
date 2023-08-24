from datetime import datetime

from fastapi import Request, HTTPException, Depends, status
from jose import jwt, JWTError

# в этом файле используем функцию depends
from app.config import settings
from app.exceptions import TokenExpiredException, IncorrectTokenFormatException, TokenAbsentException
from app.users.dao import UsersDAO


def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise TokenAbsentException
    return token

# token = get_token() писать нельзя! функция существует в рамках одного эндпоинта
# используеем depends до самого эндпоинта
# depends грубо говоря вызывает функцию


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except JWTError:
        raise IncorrectTokenFormatException
    expire = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpiredException
    user_id: int = payload.get('sub')
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return user
