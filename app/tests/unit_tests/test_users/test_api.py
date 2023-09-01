from httpx import AsyncClient
import pytest


# прописывай pytest -v, больше инфы станет видно в консоли
@pytest.mark.parametrize("email,password, status_code", [
    ("kot@pes.com", "kotopes", 200),
    ("kot@pes.com", "kot0pes", 409)
])
async def test_register_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post("/auth/register", json={
        "email": email,
        "password": password
    })

    assert response.status_code == status_code
