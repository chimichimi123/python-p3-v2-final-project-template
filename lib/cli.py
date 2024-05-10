# lib/cli.py

import cmd
from database import add_author, add_book, delete_book, display_all_books, get_all_authors, get_books_by_author, get_book_by_id
from API import get_book_info

class LibraryCLI(cmd.Cmd):
    intro = "Welcome to the Library Management System. Type 'help' for a list of commands or 'quit' to exit."
    prompt = "> "

    def do_add_author(self, name):
        add_author(name)
        print(f"Author '{name}' added successfully!")

    def do_add_book(self, isbn):
        book_info = get_book_info(isbn)
        if book_info is not None:
            title = book_info['title']
            author_name = book_info['authors'][0]
            genre = book_info['categories'][0]
            add_book(title, author_name, genre, isbn)
            print(f"Book '{title}' by {author_name} added successfully!")
        else:
            print(f"No book found with ISBN {isbn}.")

    def do_delete_book(self, book_id):
        try:
            book_id = int(book_id)
        except ValueError:
            print("Invalid book ID.")
            return
        delete_book(book_id)
        print("Book deleted successfully!")

    def do_display_books(self, args):
        books = display_all_books()
        for book in books:
            print(f"{book.id}: {book.title} by {book.author.name} ({book.genre})")

    def do_search_author(self, author_name):
        books = get_books_by_author(author_name)
        if not books:
            print(f"No books found by author {author_name}.")
        else:
            for book in books:
                print(f"{book.id}: {book.title} by {book.author.name} ({book.genre})")

    def do_display_authors(self, args):
        authors = get_all_authors()
        for i, author in enumerate(authors, start=1):
            print(f"{i}: {author.name}")

    def do_get_book(self, book_id):
        try:
            book_id = int(book_id)
        except ValueError:
            print("Invalid book ID.")
            return
        book = get_book_by_id(book_id)
        if book:
            print(f"{book.id}: {book.title} by {book.author.name} ({book.genre})")
        else:
            print(f"No book found with ID {book_id}.")

    def do_quit(self, args):
        print("Exiting...")
        return True

if __name__ == "__main__":
    LibraryCLI().cmdloop()