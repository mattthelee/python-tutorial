from fastapi import FastAPI
import uvicorn
import time
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)


def create_app():
    app = FastAPI(
        title="Server",
        description="training server",
        version="0.0.1",
    )
    
app.get("/say-hello")
async def hello():
    return {"message": "Hello World"}
    
@app.get("/time")
async def time():
    current_time = now.strftime("%H:%M:%S")
    return {"Current Time =", current_time}

app.get("/say-bye")
async def goodbye():
    return {"message": "Goodbye World"}
