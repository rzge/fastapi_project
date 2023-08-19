from fastapi import FastAPI
from typing import Optional
from datetime import date

app = FastAPI()


@app.get("/hotels")
def get_hotels(location: str,
               date_from: date,
               date_to: date,
               stars: Optional[int] = None,
               has_spa: Optional[bool] = None):
    return date_from, date_to
