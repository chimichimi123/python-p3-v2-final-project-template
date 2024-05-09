from base import Base, engine, Session
from models.book import Book

Base.metadata.create_all(engine)

def add_book(title, author, genre, isbn):
    """
    Parameters:
    title (str): The title of the book
    author (str): The author of the book
    genre (str): The genre of the book
    isbn (str): The ISBN of the book
    """
    new_book = Book(title=title, author=author, genre=genre, isbn=isbn)
    try:
        with Session() as session:
            session.add(new_book)
            session.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

def delete_book(book_id):
    """
    Parameters:
    book_id (int): The ID of the book to delete
    """
    try:
        with Session() as session:
            book = session.query(Book).filter(Book.id == book_id).one()
            session.delete(book)
            session.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

def display_all_books():
    """
    Returns a list of all books in the database
    """
    try:
        with Session() as session:
            books = session.query(Book).all()
            return books
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

def get_all_authors():
    session = Session()
    authors = session.query(Book.author).distinct().all()
    session.close()
    return authors

def get_books_by_author(author):
    session = Session()
    books = session.query(Book).filter(Book.author == author).all()
    session.close()
    return books

def get_book_by_id(book_id):
    session = Session()
    book = session.query(Book).filter(Book.id == book_id).one()
    session.close()
    return book