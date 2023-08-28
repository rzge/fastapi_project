from celery import Celery

celery = Celery(
    "tasks",
    broker="redis://localhost:6379",
    include=["app.tasks.tasks"]  # папка, где хранятся задачки
)
# команда для запуска celery -A app.tasks.celery:celery worker --loglevel=INFO --pool=solo
