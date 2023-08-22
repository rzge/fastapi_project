from fastapi import APIRouter
from sqlalchemy import select

from app.bookings.dao import BookingDAO
from app.bookings.models import Bookings
from app.database import async_session_maker

router = APIRouter(
    prefix="/bookings",
    tags=['Бронирование']  # Объединяет в swagger'e
)


@router.get("")  # дописывается в /bookings
async def get_bookings():
    result = await BookingDAO.find_all()
    return result
    # async with async_session_maker() as session:
    #     query = select(Bookings)  # SELECT * FROM bookings;
    #     result = await session.execute(query)
    #     return result.mappings().all()
