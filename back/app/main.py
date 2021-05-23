from fastapi import FastAPI
import redis
import os

r = redis.Redis(host=os.getenv('REDIS_SERVICE_HOST', 'localhost'), port=6379, db=0)
app = FastAPI()
r.set('counter', '0')


@app.get("/")
async def root():
    return {"status": "ok"}


@app.get("/count")
async def count():
    counter = int(r.get('counter'))
    r.set('counter', f'{counter+1}')
    return {"count": f"{counter}"}
