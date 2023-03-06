from fastapi import FastAPI
import time
from datetime import datetime
<<<<<<< HEAD
from fastapi import FastAPI
=======
>>>>>>> main
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
    return app

app = create_app()

<<<<<<< HEAD

=======
@app.get("/")
async def main():
    print('Hello ...')
    time.sleep(5)
    print('... World!')

    
>>>>>>> main
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

<<<<<<< HEAD
=======
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

>>>>>>> main

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
<<<<<<< HEAD
    discount: Union[float, None] = None
    location: str
    stock: float
=======
    tax: Union[float, None] = None
>>>>>>> main


@app.post("/items/")
async def create_item(item: Item):
<<<<<<< HEAD
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
=======
    return item
>>>>>>> main
