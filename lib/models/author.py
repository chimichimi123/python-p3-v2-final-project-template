from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    books = relationship('Book', back_populates='author')

    def __repr__(self):
        return f"<Author(name='{self.name}')>"