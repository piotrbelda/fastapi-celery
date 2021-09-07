from fastapi import FastAPI
from celery import Celery

app = FastAPI()

celery = Celery(
    __name__,
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0"
)

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@celery.task
def divide(x,y):
    import time
    time.sleep(10)
    return x/y