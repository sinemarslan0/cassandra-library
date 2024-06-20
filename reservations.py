from connection import get_connection
from uuid import uuid4


def add_reservation(book_id, user_id, reservation_date, status):
    session = get_connection()
    reservation_id = uuid4()
    query = """
    INSERT INTO reservations (reservation_id, book_id, user_id, reservation_date, status) 
    VALUES (%s, %s, %s, %s, %s)
    """
    session.execute(query, (reservation_id, book_id, user_id, reservation_date, status))
    return reservation_id


def get_reservation(reservation_id):
    session = get_connection()
    query = "SELECT * FROM reservations WHERE reservation_id=%s"
    result = session.execute(query, (reservation_id,))
    return result.one()


def update_reservation(reservation_id, status=None):
    session = get_connection()
    update_fields = []
    params = []
    if status:
        update_fields.append("status=%s")
        params.append(status)

    params.append(reservation_id)
    query = f"UPDATE reservations SET {', '.join(update_fields)} WHERE reservation_id=%s"
    session.execute(query, params)


def delete_reservation(reservation_id):
    session = get_connection()
    query = "DELETE FROM reservations WHERE reservation_id=%s"
    session.execute(query, (reservation_id,))
