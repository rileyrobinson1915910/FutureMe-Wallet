import sqlite3


def get_connection():
    connection = sqlite3.connect('users_name.db')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_info (
            name TEXT PRIMARY KEY,
            age INTEGER,
            income REAL,
            savings REAL,
            spending REAL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lessons_completed (
            name TEXT,
            lesson_id INTEGER,
            PRIMARY KEY (name, lesson_id)
        )
    """)
    connection.commit()
    return connection, cursor


def get_user(cursor, name):
    cursor.execute(
        "SELECT name, age, income, savings, spending FROM user_info WHERE name = ?",
        (name,)
    )
    return cursor.fetchone()


def insert_user(cursor, connection, name, age, income, savings, spending):
    cursor.execute(
        "INSERT INTO user_info VALUES (?, ?, ?, ?, ?)",
        (name, age, income, savings, spending)
    )
    connection.commit()


def update_user_field(cursor, connection, name, field, new_value):
    query = f"UPDATE user_info SET {field} = ? WHERE name = ?"
    cursor.execute(query, (new_value, name))
    connection.commit()

def mark_lesson_complete(cursor, connection, name, lesson_id): 
    cursor.execute(
        "INSERT OR IGNORE INTO lessons_completed VALUES (?, ?)",
        (name, lesson_id)
    )
    connection.commit()

