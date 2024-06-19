from books import add_book, update_book, delete_book, get_book

def test_books():
    # Add a book
    book_id = add_book("Test Book", "Test Author", "2023-06-19", "Fiction", True)
    print(f"Added book with ID: {book_id}")

    # Retrieve the book
    book = get_book(book_id)
    print(f"Retrieved book: {book}")

    # Update the book
    update_book(book_id, title="Updated Test Book", available=False)
    updated_book = get_book(book_id)
    print(f"Updated book: {updated_book}")

    # Delete the book
    delete_book(book_id)
    deleted_book = get_book(book_id)
    print(f"Deleted book: {deleted_book}")

if __name__ == "__main__":
    test_books()
