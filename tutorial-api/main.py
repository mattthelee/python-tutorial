from fastapi import FastAPI
import uvicorn
import time
import random
from datetime import datetime
from typing import Union
from pydantic import BaseModel

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


@app.get("/time")
async def time():
    current_time = now.strftime("%H:%M:%S")
    return {"Current Time =", current_time}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")


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
