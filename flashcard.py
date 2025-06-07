import sqlite3
import logger


class FlashcardManager:
    def __init__(self):
        self.conn = sqlite3.connect("flashcard_app.db")
        self.cursor = self.conn.cursor()

    def add_flashcard(self, question, answer):
        if not question or not answer:
            print("Question and answer cannot be empty.")
            return
        self.cursor.execute(
            "INSERT INTO flashcards (question, answer) VALUES (?, ?)",
            (question, answer),
        )
        self.conn.commit()
        logger.log_info(f"Added flashcard: {question}")

    def show_flashcards(self):
        self.cursor.execute("SELECT question, answer FROM flashcards")
        cards = self.cursor.fetchall()
        if not cards:
            print("No flashcards found.")
        for i, (q, a) in enumerate(cards, 1):
            print(f"{i}. Q: {q} | A: {a}")
