
from app.abstracts.abstract_repository import AbstractRepository
from app.books.book_model import Book
from app.books.schemas import BookCreate, BookUpdate
from app.database import db


class BookRepository(AbstractRepository[Book, BookCreate, BookUpdate]):
    def __init__(self, db):
        super().__init__(Book, db["books"])


book_repo = BookRepository(db)