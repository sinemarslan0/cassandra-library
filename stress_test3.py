from reservations import add_reservation
from concurrent.futures import ThreadPoolExecutor


def reserve_all_books(client_id):
    for book_id in range(1, 1001):  # Assuming 1000 books for the test
        try:
            add_reservation(f"book_id_{book_id}", f"user_id_{client_id}", "2023-06-19 10:00:00", "active")
        except Exception as e:
            print(f"Error: {e}")


def stress_test_3():
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [
            executor.submit(reserve_all_books, "client_1"),
            executor.submit(reserve_all_books, "client_2")
        ]
        for future in futures:
            try:
                future.result()
            except Exception as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    stress_test_3()
