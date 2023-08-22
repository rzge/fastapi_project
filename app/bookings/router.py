from fastapi import APIRouter

router = APIRouter(
    prefix="/bookings",
    tags=['Бронирование']  # Объединяет в swagger'e
)


@router.get("")  # дописывается в /bookings
def get_bookings():
    pass


@router.get("/{booking_id}")
def get_bookings2(booking_id):
    pass
