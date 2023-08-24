from fastapi import HTTPException, status


# правильный стиль написания кастомных исключений
class BookingException(HTTPException):  # <-- наследуемся от HTTPException, который наследован от Exception
    status_code = 500  # <-- задаем значения по умолчанию
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(BookingException):  # <-- обязательно наследуемся от нашего класса
    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь уже существует"


# неправильный стиль написания кастомных исключений
IncorrectEmailOrPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверная почта или пароль"
)

TokenExpiredException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Токен истёк"
)

TokenAbsentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Токен отсутствует"
)

IncorrectTokenFormatException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверный формат токена",
)
