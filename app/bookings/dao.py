# файл для работы с базой данных
# DAO - data access object
from sqlalchemy import select

from app.bookings.models import Bookings
from app.database import async_session_maker


class BookingDAO:

    @classmethod
    async def find_all(cls):
        # если не использовать classmethod, то придётся
        # писать bookings = BookingDAO(); bookings.find_all(),
        # а с классметодом всего лишь BookingDAO.find_all()
        async with async_session_maker() as session:
            query = select(Bookings)
            bookings = await session.execute(query)
            return bookings.mappings().all()  # эту конструкцию можно вызвать только один раз!
