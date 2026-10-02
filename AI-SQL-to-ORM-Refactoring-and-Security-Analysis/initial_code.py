#!/usr/bin/python3
"""Original procedural MySQL example using raw SQL."""

import mysql.connector
from mysql.connector import Error


def get_connection():
    """Establish and return a database connection."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="example_db"
    )


def create_user(db_cursor, username, email):
    """Create a new user safely using parameterized queries."""
    if not username or not email:
        print("Username and email are required.")
        return

    sql = "INSERT INTO users (username, email) VALUES (%s, %s)"

    try:
        db_cursor.execute(sql, (username, email))
        print(f"User '{username}' created successfully.")
    except Error as e:
        print(f"Error creating user: {e}")


def get_user_by_username(db_cursor, username):
    """Fetch a single user by username."""
    sql = (
        "SELECT id, username, email, created_at "
        "FROM users WHERE username = %s"
    )

    db_cursor.execute(sql, (username,))
    result = db_cursor.fetchone()

    if result:
        print("User found:", result)
    else:
        print("No user found with that username.")

    return result


def update_user_email(db_cursor, username, new_email):
    """Update the user's email."""
    sql = "UPDATE users SET email = %s WHERE username = %s"
    db_cursor.execute(sql, (new_email, username))

    if db_cursor.rowcount:
        print(f"Email for '{username}' updated to '{new_email}'.")
    else:
        print("No user found to update.")


def delete_user(db_cursor, username):
    """Delete a user by username."""
    sql = "DELETE FROM users WHERE username = %s"
    db_cursor.execute(sql, (username,))

    if db_cursor.rowcount:
        print(f"User '{username}' deleted.")
    else:
        print("No user found to delete.")


def list_users(db_cursor, limit=5):
    """List users with a limit."""
    sql = (
        "SELECT id, username, email, created_at "
        "FROM users ORDER BY created_at DESC LIMIT %s"
    )

    db_cursor.execute(sql, (limit,))
    users = db_cursor.fetchall()

    for user in users:
        print(user)

    return users
