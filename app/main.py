from fastapi import FastAPI

app = FastAPI()

@app.get("/hotels")
def get_hotels():
    return 'Отель бридж резорт 5 звёзд'