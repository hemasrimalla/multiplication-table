"""
Multiplication Table Generator
A beginner-friendly Python program to generate multiplication tables.
"""

def print_table(number: int, limit: int) -> None:
    """
    Print the multiplication table for a given number up to a specified limit.
    
    Parameters:
        number (int): The number whose multiplication table is generated.
        limit (int): The positive integer up to which the table runs.
    """
    header = f"Multiplication Table of {number}"
    print(f"\n{header}")
    print("-" * max(len(header), 25))

    # Calculate padding widths so columns align cleanly regardless of input sizes
    limit_width = len(str(limit))
    max_result = max(abs(number * 1), abs(number * limit))
    # Account for minus sign if the number is negative
    result_width = max(len(str(max_result)) + (1 if number < 0 else 0), 3)

    # Use a for loop with range() from 1 up to and including the limit
    for i in range(1, limit + 1):
        product = number * i
        # Align multiplier and product for a neat columnar display
        print(f"{number} x {i:>{limit_width}} = {product:>{result_width}}")
    print()


def get_integer_input(prompt: str) -> int:
    """
    Prompt the user to enter an integer.
    Re-prompts continuously if the input cannot be parsed as an integer.
    """
    while True:
        user_input = input(prompt).strip()
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid whole number (integer).")


def get_positive_integer_input(prompt: str) -> int:
    """
    Prompt the user to enter a positive integer (> 0).
    Re-prompts if the input is not a positive integer.
    """
    while True:
        value = get_integer_input(prompt)
        if value > 0:
            return value
        print("Invalid input. The limit must be a positive integer greater than 0.")


def main() -> None:
    """
    Main function to run the interactive multiplication table generator.
    Allows generating multiple tables until the user decides to quit.
    """
    print("========================================")
    print("    Multiplication Table Generator     ")
    print("========================================")

    # Main application loop
    while True:
        # Step 1: Prompt for the number and limit with validation
        number = get_integer_input("\nEnter a number: ")
        limit = get_positive_integer_input("Enter the limit (e.g., 10, 12, 20): ")

        # Step 2: Generate and display the table
        print_table(number, limit)

        # Step 3: Ask the user if they want to generate another table or quit
        while True:
            choice = input("Do you want to generate another table? (y/n): ").strip().lower()
            if choice in ("y", "yes"):
                break
            elif choice in ("n", "no"):
                print("\nThank you for using the Multiplication Table Generator. Goodbye!")
                return
            else:
                print("Invalid choice. Please enter 'y' to continue or 'n' to quit.")


if __name__ == "__main__":
    main()
