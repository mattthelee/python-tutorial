from fastapi import FastAPI
import uvicorn
import time
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union


now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)


def create_app():
    app = FastAPI(
        title="Server",
        description="training server",
        version="0.0.1"
    )
    
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


@app.post("/items/")
async def create_item(item: Item):
    return item

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