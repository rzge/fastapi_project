from app.users.dao import UsersDAO

async def test_find_user_by_id():
    user = await UsersDAO.find_by_id(1)

    assert user.email == 'test@test.com'
    assert user.id == 1