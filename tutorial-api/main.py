from fastapi import FastAPI
import time
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)


app = create_app()

def create_app():
    app = FastAPI(
        title="Server",
        description="training server",
        version="0.0.1",
    )
    
@app.get("/")
async def main():
    print('Hello ...')
    time.sleep(5)
    print('... World!')
    
@app.get("/time")
async def time():
    current_time = now.strftime("%H:%M:%S")
    return {"Current Time =", current_time}
