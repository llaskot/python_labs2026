from app.abstracts import AbstractService
from .repository import book_repo
from .schemas import BookCreate, BookUpdate


class BookService(AbstractService[BookCreate, BookUpdate]):
    def __init__(self):
        super().__init__(book_repo)