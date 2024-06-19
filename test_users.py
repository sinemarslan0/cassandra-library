from users import add_user, update_user, delete_user, get_user


def test_users():
    # Add a user
    user_id = add_user("Test User", "testuser@example.com", "2023-06-19")
    print(f"Added user with ID: {user_id}")

    # Retrieve the user
    user = get_user(user_id)
    print(f"Retrieved user: {user}")

    # Update the user
    update_user(user_id, name="Updated Test User", email="updateduser@example.com")
    updated_user = get_user(user_id)
    print(f"Updated user: {updated_user}")

    # Delete the user
    delete_user(user_id)
    deleted_user = get_user(user_id)
    print(f"Deleted user: {deleted_user}")


if __name__ == "__main__":
    test_users()
