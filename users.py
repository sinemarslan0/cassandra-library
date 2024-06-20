from connection import get_connection
from uuid import uuid4


def add_user(name, email, join_date):
    session = get_connection()
    user_id = uuid4()
    query = """
    INSERT INTO users (user_id, name, email, join_date) 
    VALUES (%s, %s, %s, %s)
    """
    session.execute(query, (user_id, name, email, join_date))
    return user_id


def get_user(user_id):
    session = get_connection()
    query = "SELECT * FROM users WHERE user_id=%s"
    result = session.execute(query, (user_id,))
    return result.one()


def update_user(user_id, name=None, email=None, join_date=None):
    session = get_connection()
    update_fields = []
    params = []
    if name:
        update_fields.append("name=%s")
        params.append(name)
    if email:
        update_fields.append("email=%s")
        params.append(email)
    if join_date:
        update_fields.append("join_date=%s")
        params.append(join_date)

    params.append(user_id)
    query = f"UPDATE users SET {', '.join(update_fields)} WHERE user_id=%s"
    session.execute(query, params)


def delete_user(user_id):
    session = get_connection()
    query = "DELETE FROM users WHERE user_id=%s"
    session.execute(query, (user_id,))
