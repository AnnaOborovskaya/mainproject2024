from fastapi import FastAPI
from fastapi.responses import FileResponse
from public.users import users_router
from public.orders import orders_router
import uvicorn
from db import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(users_router)
app.include_router(orders_router)

@app.on_event("startup")
async def on_startup():
    open("log.txt", mode="a").write(f'{datetime.utcnow()}: Begin\n')
    await create_tables()

@app.on_event("shutdown")
async def shutdown():
    open("log.txt", mode="a").write(f'{datetime.utcnow()}: End\n')
    
@app.get('/')
async def main():
    return FileResponse("files/index.html")
