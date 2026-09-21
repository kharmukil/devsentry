from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.app.api.chat import router as chat_router

app = FastAPI(
    title="DevSentry",
    description="AI-powered DevOps assistant for cloud troubleshooting and incident analysis",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8001", "http://localhost:8001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "DevSentry",
    }
