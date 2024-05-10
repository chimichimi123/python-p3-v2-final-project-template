from models.base import Base, engine, Session
from models.book import Book
from models.author import Author

Base.metadata.create_all(engine)

def add_author(name):
    new_author = Author(name=name)
    try:
        with Session() as session:
            session.add(new_author)
            session.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

def add_book(title, author_name, genre, isbn):
    try:
        with Session() as session:
            author = session.query(Author).filter(Author.name == author_name).one_or_none()
            if author is None:
                author = Author(name=author_name)
                session.add(author)
            new_book = Book(title=title, author=author, genre=genre, isbn=isbn)
            session.add(new_book)
            session.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

def delete_book(book_id):
    try:
        with Session() as session:
            book = session.query(Book).filter(Book.id == book_id).one()
            session.delete(book)
            session.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

def display_all_books():
    try:
        with Session() as session:
            books = session.query(Book).all()
            return books
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

def get_all_authors():
    try:
        with Session() as session:
            authors = session.query(Author).all()
            return authors
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

def get_books_by_author(author_name):
    try:
        with Session() as session:
            author = session.query(Author).filter(Author.name == author_name).one()
            books = author.books
            return books
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

def get_book_by_id(book_id):
    try:
        with Session() as session:
            book = session.query(Book).filter(Book.id == book_id).one()
            return book
    except Exception as e:
        print(f"An error occurred: {e}")
        raise