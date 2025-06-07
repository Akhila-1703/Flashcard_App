import sqlite3


def setup_database():
    conn = sqlite3.connect("flashcard_app.db")
    cursor = conn.cursor()

    # Flashcards
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS flashcards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    """)

    # Calculator
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS calculations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            expression TEXT NOT NULL,
            result TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()
