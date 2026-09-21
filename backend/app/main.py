from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.app.api.chat import router as chat_router
from backend.app.api.logs import router as logs_router


app = FastAPI(title="DevSentry")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "DevSentry",
    }


app.include_router(chat_router)
app.include_router(logs_router)


app.mount(
    "/",
    StaticFiles(directory="frontend", html=True),
    name="frontend",
)