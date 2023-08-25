from datetime import date

from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy import select

from app.bookings.dao import BookingDAO
from app.bookings.models import Bookings
from app.database import async_session_maker
from app.hotels.dao import HotelDAO
from app.users.dependecies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/hotels",
    tags=['Отели']  # Объединяет в swagger'e
)


@router.get("")  # дописывается в /bookings
async def get_hotels_by_location(location: str):
    hotels = await HotelDAO.search_for_hotels(location=location)
    if not hotels:
        raise HTTPException(status_code=404, detail="Локация не найдена")
    return hotels
