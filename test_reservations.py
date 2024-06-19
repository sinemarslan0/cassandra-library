from reservations import add_reservation, update_reservation, delete_reservation, get_reservation

def test_reservations():
    # Add a reservation
    reservation_id = add_reservation("book_id_example", "user_id_example", "2023-06-19 10:00:00", "active")
    print(f"Added reservation with ID: {reservation_id}")

    # Retrieve the reservation
    reservation = get_reservation(reservation_id)
    print(f"Retrieved reservation: {reservation}")

    # Update the reservation
    update_reservation(reservation_id, status="completed")
    updated_reservation = get_reservation(reservation_id)
    print(f"Updated reservation: {updated_reservation}")

    # Delete the reservation
    delete_reservation(reservation_id)
    deleted_reservation = get_reservation(reservation_id)
    print(f"Deleted reservation: {deleted_reservation}")

if __name__ == "__main__":
    test_reservations()
