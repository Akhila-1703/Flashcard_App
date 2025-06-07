import sqlite3

class FlashcardApp:
    def __init__(self):
        self.conn = sqlite3.connect('flashcards.db')
        self.cursor = self.conn.cursor()
        self.create_table()
        self.score = 0

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS flashcards (
                id INTEGER PRIMARY KEY,
                question TEXT NOT NULL,
                answer TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def add_flashcard(self):
        question = input("Enter question: ")
        answer = input("Enter answer: ")
        self.cursor.execute("INSERT INTO flashcards (question, answer) VALUES (?, ?)", (question, answer))
        self.conn.commit()
        print("Flashcard added successfully.")

    def take_quiz(self):
        self.cursor.execute("SELECT * FROM flashcards")
        cards = self.cursor.fetchall()
        score = 0
        for card in cards:
            print(f"Question: {card[1]}")
            user_answer = input("Your answer: ")
            if user_answer.strip().lower() == card[2].strip().lower():
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! Correct answer: {card[2]}")
        self.score = score
        print(f"Your score: {self.score}/{len(cards)}")

    def view_flashcards(self):
        self.cursor.execute("SELECT * FROM flashcards")
        cards = self.cursor.fetchall()
        for card in cards:
            print(f"Q: {card[1]} | A: {card[2]}")

    def run(self):
        while True:
            print("\n1. Add Flashcard\n2. Take Quiz\n3. View Flashcards\n4. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.add_flashcard()
            elif choice == '2':
                self.take_quiz()
            elif choice == '3':
                self.view_flashcards()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Try again.")