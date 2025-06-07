import sqlite3
import logger


class Quiz:
    def __init__(self, flashcard_manager):
        self.flashcard_manager = flashcard_manager

    def start(self):
        conn = sqlite3.connect("flashcard_app.db")
        cursor = conn.cursor()
        cursor.execute("SELECT question, answer FROM flashcards")
        flashcards = cursor.fetchall()
        if not flashcards:
            print("No flashcards available for quiz.")
            return

        score = 0
        for question, answer in flashcards:
            print(f"\nQuestion: {question}")
            user_ans = input("Your Answer: ").strip()
            if user_ans.lower() == answer.lower():
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect! Correct answer was: {answer}")

        print(f"\nYour Score: {score}/{len(flashcards)}")
        logger.log_info(f"Quiz completed. Score: {score}/{len(flashcards)}")
