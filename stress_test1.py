from books import add_book
from concurrent.futures import ThreadPoolExecutor


def stress_test_1():
    def task():
        add_book("Stress Test Book", "Stress Test Author", "2023-06-19", "Fiction", True)

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(task) for _ in range(10000)]
        for future in futures:
            try:
                future.result()
            except Exception as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    stress_test_1()
