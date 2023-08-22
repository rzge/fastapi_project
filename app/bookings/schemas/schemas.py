# файл для хранения схема
from datetime import date
from typing import Optional

from pydantic import BaseModel


class SBooking(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: Optional[int] = None
    total_days: Optional[int] = None

    class Config:
        orm_mode = True  # чтоб если что, можно было бы обращаться через точку, а не через скобки
