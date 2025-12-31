from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.db.database import init_db
from app.config import ENV
from app.routers import documents
from app.routers import search


@asynccontextmanager
async def lifespan(app: FastAPI):
    if ENV == "development":
        init_db()
    yield


app = FastAPI(
    title="RAG German Docs",
    lifespan=lifespan,
)

app.include_router(documents.router)
app.include_router(search.router)
