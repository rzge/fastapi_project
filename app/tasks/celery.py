from celery import Celery
from app.config import settings
celery = Celery(
    "tasks",
    broker=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
    include=["app.tasks.tasks"]  # папка, где хранятся задачки
)
# команда для запуска celery -A app.tasks.celery:celery worker --loglevel=INFO --pool=solo
