from flashcard import FlashcardManager
from quiz import Quiz
from calculator import Calculator
from database import setup_database


def main():
    setup_database()
    manager = FlashcardManager()
    quiz = Quiz(manager)
    calculator = Calculator()

    while True:
        print("\n--- Main Menu ---")
        print("1. Flashcards")
        print("2. Quiz")
        print("3. Calculator")
        print("4. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            flashcard_menu(manager)
        elif choice == "2":
            quiz.start()
        elif choice == "3":
            calculator.run()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


def flashcard_menu(manager):
    while True:
        print("\n--- Flashcard Menu ---")
        print("1. Add Flashcard")
        print("2. View Flashcards")
        print("3. Back to Main Menu")

        sub = input("Choose an option: ").strip()
        if sub == "1":
            q = input("Enter question: ").strip()
            a = input("Enter answer: ").strip()
            manager.add_flashcard(q, a)
        elif sub == "2":
            manager.show_flashcards()
        elif sub == "3":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
