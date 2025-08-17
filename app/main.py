from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)
print("Backend started successfully!")  # Add this

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/health")
def health():
    return {"status": "ok"}

import socket
from fastapi import APIRouter

self_test = APIRouter()

@self_test.get("/selftest")
async def selftest():
    hostname = socket.gethostname()
    return {
        "status": "running",
        "host": hostname
    }

app.include_router(self_test)
