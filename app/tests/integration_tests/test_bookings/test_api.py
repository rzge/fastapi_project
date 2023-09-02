from datetime import datetime

import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("room_id,date_from,date_to,status_code", [
    *[(4, "2030-05-01", "2030-05-15", 200)] * 8,
    (4, "2030-05-01", "2030-05-15", 409)
])  # 9 раз должна вернуться ошибка
async def test_add_and_get_booking(room_id, date_from, date_to, status_code, authenticated_ac: AsyncClient):
    response = await authenticated_ac.post("/bookings", params={
        "room_id": room_id,
        "date_from": datetime.strptime(date_from, "%Y-%m-%d"),
        "date_to": datetime.strptime(date_to, "%Y-%m-%d")
    })  # json используется для pydantic моделей
    assert response.status_code == status_code
