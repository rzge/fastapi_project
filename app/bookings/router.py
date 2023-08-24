from fastapi import APIRouter, Request, Depends
from sqlalchemy import select

from app.bookings.dao import BookingDAO
from app.bookings.models import Bookings
from app.database import async_session_maker
from app.users.dependecies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=['Бронирование']  # Объединяет в swagger'e
)


@router.get("")  # дописывается в /bookings
async def get_bookings(user: Users = Depends(get_current_user)):
    # print(user, type(user), user.email)
    return await BookingDAO.find_all(user_id=user.id)
    # return await BookingDAO.find_all()
    # result = await BookingDAO.find_all()
    # return result

    # async with async_session_maker() as session:
    #     query = select(Bookings)  # SELECT * FROM bookings;
    #     result = await session.execute(query)
    #     return result.mappings().all()
