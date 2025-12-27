from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.db.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    yield
    # Shutdown (nothing yet)


app = FastAPI(
    title="RAG German Docs",
    lifespan=lifespan,
)


@app.get("/health")
def health_check():
    return {"status": "ok"}
