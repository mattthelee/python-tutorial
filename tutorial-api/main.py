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

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

class User(BaseModel):
    name: str
    email: str
    age: int
    gender: str
    
numbers_db = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def create_app():
    app = FastAPI(
        title="Server",
        description="training server",
        version="0.0.1"
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


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    discount: Union[float, None] = None
    location: str
    stock: float


goodbye_msg = ["Goodbye", "See ya", "Auf Wiedersehen"]


@app.get("/website_msg/")
async def goodbye(goodbye_msg):
    print(goodbye_msg[random.randint(0, len(goodbye_msg) - 1)])
    return


@app.post("/items/")
async def create_item(item: Item):
    return item


@app.get("/items/sale")
async def create_item_discount(item: Item):
    if item.stock <= 2:
       new_price = item.price / item.discount
    return ({"Price with discount": new_price})



@app.get("/about")
async def about():
    return {'''


    Welcome to this test server
    Here you will see we have made an about page...
    This is the first server we made :)
    
    '''
    }
