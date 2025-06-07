import logger
import sqlite3


class Calculator:
    def run(self):
        while True:
            print("\n--- Calculator ---")
            print("Enter 'exit' to return to main menu.")
            expr = input("Enter arithmetic expression (e.g., 5 + 2): ").strip()
            if expr.lower() == "exit":
                break
            try:
                result = self.evaluate(expr)
                print(f"Result: {result}")
                self.save_to_db(expr, result)
                logger.log_info(f"Calculation: {expr} = {result}")
            except Exception as e:
                print(f"Error: {e}")
                logger.log_error(f"Calculation error for '{expr}': {e}")

    def evaluate(self, expression):
        allowed = "+-*/.0123456789() "
        if any(c not in allowed for c in expression):
            raise ValueError("Invalid characters in expression.")
        return eval(expression)

    def save_to_db(self, expression, result):
        conn = sqlite3.connect("flashcard_app.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO calculations (expression, result) VALUES (?, ?)",
            (expression, result),
        )
        conn.commit()
        conn.close()
