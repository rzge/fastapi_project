from sqladmin import ModelView

from app.users.models import Users


class UsersAdmin(ModelView, model=Users):
    column_list = [Users.id, Users.email]
    column_details_exclude_list = [Users.hashed_password] # прячем пароль
    can_delete = False
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"
