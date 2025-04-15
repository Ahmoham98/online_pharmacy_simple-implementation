from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from http import HTTPStatus
from .service import BookService
from .schemas import BookCreateModel, BookResponseModel

book_router = APIRouter(
    prefix="/books",
)


@book_router.get("/", response_model=list[BookResponseModel])
async def read_books(session: AsyncSession = Depends(get_session)):
    books = await BookService(session=session).get_all_books()
    return books

@book_router.post("/", response_model=BookCreateModel , status_code=HTTPStatus.CREATED)
async def create_book(
    book_create_data: BookCreateModel,
    session: AsyncSession = Depends(get_session)
):
    new_book = await BookService(session=session).create_book(book_create_data)
    return new_book

@book_router.get("/{book_id}", status_code=HTTPStatus.OK)
async def read_book(book_id: str, session: AsyncSession = Depends(get_session)):
    book = await BookService(session=session).get_book(book_uid=book_id)
    return book

@book_router.put("/{book_id}", status_code=HTTPStatus.OK)
async def update_book(
    book_id: str,
    update_book: BookCreateModel,
    session: AsyncSession = Depends(get_session)):
    
    update_book = await BookService(session=session).update_book(book_id, update_book=update_book)
    return {"massega": "updated successfully! "}

@book_router.delete("/", status_code=HTTPStatus.NO_CONTENT)
async def delete_book(book_id: str, session: AsyncSession = Depends(get_session)):
    await BookService(session=session).delete_book(book_uid=book_id)
    return {"message": "data deleted successfully"}

