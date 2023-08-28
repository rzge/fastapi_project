from app.tasks.celery import celery
from PIL import Image
from pathlib import Path


# в данном файле присутствуют задачи обработки и сжатия фотографий


@celery.task
def process_pic(
        path: str,
):
    im_path = Path(path)  # str -> Path
    im = Image.open(im_path)
    im_resized_1000_500 = im.resize((1000, 500))
    im_resized_200_100 = im.resize((200, 100))
    im_resized_1000_500.save(f"app/static/images/resized_1000_500_{im_path.name}")
    im_resized_200_100.save(f"app/static/images/resized_200_100_{im_path.name}")
