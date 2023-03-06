from fastapi import FastAPI
import time
from datetime import datetime
from pydantic import BaseModel
from typing import Union


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

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.post("/items/")
async def create_item(item: Item):
    return item