import random
from books import add_book
from users import add_user
from reservations import add_reservation
from concurrent.futures import ThreadPoolExecutor


def random_task():
    tasks = [
        lambda: add_book("Random Book", "Random Author", "2023-06-19", "Fiction", True),
        lambda: add_user("Random User", "randomuser@example.com", "2023-06-19"),
        lambda: add_reservation("book_id_example", "user_id_example", "2023-06-19 10:00:00", "active"),
    ]
    task = random.choice(tasks)
    try:
        task()
    except Exception as e:
        print(f"Error: {e}")


def stress_test_2():
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(random_task) for _ in range(10000)]
        for future in futures:
            try:
                future.result()
            except Exception as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    stress_test_2()
