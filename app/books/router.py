from fastapi import APIRouter, Response, Request, HTTPException
from pymongo.errors import DuplicateKeyError

from app.books.schemas import BookCreate, BookUpdate, BookResponse
from app.books.service import BookService

router = APIRouter(prefix="/books", tags=["Books"])


@router.post("/", response_model=BookResponse)
async def create_book(book_data: BookCreate):
    service = BookService()
    try:
        return await service.create(book_data)
    except HTTPException as http_ex:
        raise http_ex
    except DuplicateKeyError as e:
        raise HTTPException(status_code=409, detail='DuplicateFieldError') from e
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e)) from e


@router.patch("/{book_id}", response_model=BookResponse)
async def update_book(book_id: str, book_data: BookUpdate):
    service = BookService()
    try:
        return await service.update(book_id, book_data)
    except HTTPException as http_ex:
        raise http_ex
    except DuplicateKeyError as e:
        raise HTTPException(status_code=409, detail='DuplicateFieldError') from e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


@router.get("/{book_id}", response_model=BookResponse)
async def get_by_id(book_id: str):
    service = BookService()
    try:
        return await service.get_by_id(book_id)
    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


@router.get("/", response_model=list[BookResponse])
async def get_all():
    service = BookService()
    try:
        return await service.get_all()
    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


@router.delete("/{book_id}")
async def delete(book_id: str):
    service = BookService()
    try:
        return await service.delete(book_id)
    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
