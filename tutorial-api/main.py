from fastapi import FastAPI
import time
from datetime import datetime
from pydantic import BaseModel
from typing import Union

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

@app.get("/numbers/")
async def read_item(skip: int = 0, limit: int = 10):
    return numbers_db[skip : skip + limit]

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.post("/users/")
async def create_user(item: User):
    return item



# python -m uvicorn main:app --reload    - ignore this. it's just for easy copy/paste to run fastapi
