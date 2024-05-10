# book.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    genre = Column(String, nullable=False)
    isbn = Column(String, nullable=False, unique=True)

    author = relationship('Author', back_populates='books')
    
    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}')>"