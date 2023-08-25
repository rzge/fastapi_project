# файл для работы с базой данных
# DAO - data access object
from datetime import date

from sqlalchemy import select, and_, or_, func, insert

from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.hotels.models import Hotels


class HotelDAO(BaseDAO):
    model = Hotels

    @classmethod
    async def search_for_hotels(cls,
                                location: str):
        async with async_session_maker() as session:
            query = select(Hotels).where(Hotels.location.like(f'%{location}%'))
            result = await session.execute(query)
            return result.mappings().all()  # возвращает одно значение, или ничто