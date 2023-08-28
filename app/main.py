from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.admin.views import UsersAdmin
from app.bookings.router import router as router_bookings
from app.config import settings
from app.database import engine
from app.users.models import Users
from app.users.router import router as router_users
from app.pages.router import router as router_pages
from app.hotels.router import router as router_hotels
from app.images.router import router as router_images
from sqladmin import Admin, ModelView
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from sqladmin import Admin, ModelView
from redis import asyncio as aioredis

app = FastAPI()
# монтируем директорию для статических файлов
app.mount("/static", StaticFiles(directory="app/static"), "static")

app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_pages)
app.include_router(router_hotels)
app.include_router(router_images)

origins = [
    "http://localhost:3000",
]  # адреса сервисов, которые могут обращаться к нашему апи. Нужно для фронтендеров
# обычно а-ля https://mysite.com. Разрешаем этому адресу использовать https://api.mysite.com
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'OPTIONS', 'DELETE', 'PATCH', 'PUT'],
    allow_headers=['Content-Type', "Set-Cookie", "Access-Control-Allow-Headers", "Access-Authorization"],
)


@app.on_event("startup")  # При старте предложения начинает прогонять функцию ниже
async def startup():
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}")
    FastAPICache.init(RedisBackend(redis), prefix="cache")

# настраиваем админку
admin = Admin(app, engine)


admin.add_view(UsersAdmin)
