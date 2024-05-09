import requests

def get_book_info(isbn):
    response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}")
    data = response.json()

    if "items" in data:
        book_info = data["items"][0]["volumeInfo"]
        return {
            "title": book_info.get("title"),
            "authors": book_info.get("authors"),
            "publisher": book_info.get("publisher"),
            "publishedDate": book_info.get("publishedDate"),
            "description": book_info.get("description"),
            "categories": book_info.get("categories"),
        }
    else:
        return None