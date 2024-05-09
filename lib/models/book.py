# book.py
from sqlalchemy import Column, Integer, String
from base import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    isbn = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}')>"