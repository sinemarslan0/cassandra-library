from connection import get_connection
from uuid import uuid4


def add_book(title, author, published_date, genre, available):
    session = get_connection()
    book_id = uuid4()
    query = """
    INSERT INTO books (book_id, title, author, published_date, genre, available) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    session.execute(query, (book_id, title, author, published_date, genre, available))
    return book_id


def get_book(book_id):
    session = get_connection()
    query = "SELECT * FROM books WHERE book_id=%s"
    result = session.execute(query, (book_id,))
    return result.one()


def update_book(book_id, title=None, author=None, published_date=None, genre=None, available=None):
    session = get_connection()
    update_fields = []
    params = []
    if title:
        update_fields.append("title=%s")
        params.append(title)
    if author:
        update_fields.append("author=%s")
        params.append(author)
    if published_date:
        update_fields.append("published_date=%s")
        params.append(published_date)
    if genre:
        update_fields.append("genre=%s")
        params.append(genre)
    if available is not None:
        update_fields.append("available=%s")
        params.append(available)

    params.append(book_id)
    query = f"UPDATE books SET {', '.join(update_fields)} WHERE book_id=%s"
    session.execute(query, params)


def delete_book(book_id):
    session = get_connection()
    query = "DELETE FROM books WHERE book_id=%s"
    session.execute(query, (book_id,))
