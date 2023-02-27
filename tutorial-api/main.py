from fastapi import FastAPI, Body, Path, HTTPException
import time


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
