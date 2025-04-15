from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.books.routes import book_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    
    await init_db()
    
    yield

app = FastAPI(
    title="Online_pharmacy_service",
    description="Online pharmacy for save time and faster reach, anytime anywhere",
    version="1.0.0",
    lifespan=lifespan
)


app.include_router(book_router, tags=["books API's"])