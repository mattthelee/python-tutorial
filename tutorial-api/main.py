from fastapi import FastAPI
import time
import random
from datetime import datetime
from typing import Union
from pydantic import BaseModel
import uvicorn

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)


def create_app():
    app = FastAPI(
        title="Server",
        description="training server",
        version="0.0.1",
    )
    return app


app = create_app()


@app.get("/")
async def main():
    print('Hello ...')
    time.sleep(5)
    print('... World!')


@app.get("/say-hello")
async def hello():
    return {"message": "Hello World"}


@app.get("/time")
async def time():
    current_time = now.strftime("%H:%M:%S")
    return {"Current Time =", current_time}


@app.get("/say-bye")
async def goodbye():
    return {"message": "Goodbye World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


goodbye_msg = ["Goodbye", "See ya", "Auf Wiedersehen"]


@app.get("/website_msg/")
async def goodbye(goodbye_msg):
    print(goodbye_msg[random.randint(0, len(goodbye_msg) - 1)])
    return


@app.post("/items/")
async def create_item(item: Item):
    return item
