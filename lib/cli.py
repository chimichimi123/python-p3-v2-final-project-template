# lib/cli.py

import cmd
from database import add_book, delete_book, display_all_books, get_books_by_author, get_all_authors, get_book_by_id
from API import get_book_info

# Defines a class for the (CLI) of the library management system
class LibraryCLI(cmd.Cmd):
    # this sets the intro and prompt for the CLI
    intro = "Welcome to the Library Management System. Type 'help' for a list of commands or 'quit' to exit."
    prompt = "> "

    
    def do_add_book(self, isbn):
        book_info = get_book_info(isbn)
        if not book_info:
            print(f"No book found with ISBN {isbn}.")
        else:
            title = book_info['title']
            author = ', '.join(book_info['authors'])
            genre = ', '.join(book_info['categories']) if book_info['categories'] else 'N/A'
            add_book(title, author, genre, isbn)
            print(f"Book '{title}' by {author} added successfully!")

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
            print(f"{book.id}: {book.title} by {book.author} ({book.genre})")

        # Askz the user for a book ID to get more info
        book_id = input("Enter the ID of a book to get more information, or 'q' to quit: ")
        if book_id.lower() != 'q':
            try:
                book = get_book_by_id(int(book_id))
                if book:
                    # Get more info about the book using the API
                    book_info = get_book_info(book.isbn)
                    if book_info:
                        print(f"Title: {book_info['title']}")
                        print(f"Authors: {', '.join(book_info['authors'])}")
                        print(f"Publisher: {book_info['publisher']}")
                        print(f"Published Date: {book_info['publishedDate']}")
                        print(f"Description: {book_info['description']}")
                        print(f"Categories: {', '.join(book_info['categories']) if book_info['categories'] else 'N/A'}")
                    else:
                        print(f"No additional information found for book with ID {book_id}.")
                else:
                    print(f"No book found with ID {book_id}.")
            except Exception as e:
                print(f"An error occurred: {e}")
            
    def do_search_author(self, author):
        books = get_books_by_author(author)
        if not books:
            print(f"No books found by author {author}.")
        else:
            for book in books:
                print(f"{book.id}: {book.title} by {book.author} ({book.genre})")
            book_id = input("Enter the ID of a book to view its details, or 'q' to quit: ")
            if book_id.lower() != 'q':
                try:
                    book = get_book_by_id(int(book_id))
                    print(f"Title: {book.title}\nAuthor: {book.author}\nGenre: {book.genre}\nISBN: {book.isbn}")
                except Exception as e:
                    print(f"An error occurred: {e}")
            
    def do_display_author(self, args):
        authors = get_all_authors()
        for i, author in enumerate(authors, start=1):
            print(f"{i}: {author}")
        author_index = input("Enter the index of an author to view all books by them, or 'q' to quit: ")
        if author_index.lower() != 'q':
            try:
                author_index = int(author_index)
                if 1 <= author_index <= len(authors):
                    author = authors[author_index - 1][0]
                    books = get_books_by_author(author)
                    if not books:
                        print(f"No books found by author {author}.")
                    else:
                        for i, book in enumerate(books, start=1):
                            print(f"{i}: {book.title} by {book.author} ({book.genre})")
                        # Asks the user for a book index to get its details
                        book_index = input("Enter the index of a book to view its details, or 'q' to quit: ")
                        if book_index.lower() != 'q':
                            try:
                                book_index = int(book_index)
                                if 1 <= book_index <= len(books):
                                    book = books[book_index - 1]
                                    print(f"Title: {book.title}\nAuthor: {book.author}\nGenre: {book.genre}\nISBN: {book.isbn}")
                                else:
                                    print("Invalid book index.")
                            except ValueError:
                                print("Invalid book index.")
                else:
                    print("Invalid author index.")
            except ValueError:
                print("Invalid author index.")
                
    def do_get_book_info(self, isbn):
        #Gets information about the book by its ISBN from the API
        book_info = get_book_info(isbn)
        if not book_info:
            print(f"No book found with ISBN {isbn}.")
        else:
            print(f"Title: {book_info['title']}")
            print(f"Authors: {', '.join(book_info['authors'])}")
            print(f"Publisher: {book_info['publisher']}")
            print(f"Published Date: {book_info['publishedDate']}")
            print(f"Description: {book_info['description']}")
            print(f"Categories: {', '.join(book_info['categories']) if book_info['categories'] else 'N/A'}")
    
    def do_quit(self, args):
        print("Exiting...")
        return True

if __name__ == "__main__":
    LibraryCLI().cmdloop()