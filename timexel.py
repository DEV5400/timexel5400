import json
from datetime import datetime

# Global variables
currency = 0
transaction_history = []


def save_data_to_file():
    data = {'currency': currency, 'transaction_history': transaction_history}
    with open('transaction_history.json', 'w') as file:
        json.dump(data, file)


def load_data_from_file():
    global currency, transaction_history
    try:
        with open('transaction_history.json', 'r') as file:
            data = json.load(file)

            if isinstance(data, dict):
                currency = data.get('currency', 0)
                transaction_history = data.get('transaction_history', [])
            else:
                # Handle the case where data is a list (backward compatibility)
                transaction_history = data
                currency = sum(
                    [int(transaction.split()[2]) for transaction in transaction_history if "Piled" in transaction])
    except FileNotFoundError:
        # File doesn't exist yet
        pass


def pile_time():
    global currency
    task_description = input("Enter task description: ")
    hours = int(input("Enter hours: "))
    minutes = int(input("Enter minutes: "))
    seconds = int(input("Enter seconds: "))

    time_added = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    transaction_history.append(f"{time_added} Piled {hours}h {minutes}m {seconds}s for '{task_description}'")

    total_seconds = hours * 3600 + minutes * 60 + seconds
    currency += total_seconds
    print(f"Time added: {hours}h {minutes}m {seconds}s")
    print(f"Current balance: {currency} seconds")


def spend_time():
    global currency
    task_description = input("Enter task description: ")
    hours = int(input("Enter hours: "))
    minutes = int(input("Enter minutes: "))
    seconds = int(input("Enter seconds: "))

    total_seconds = hours * 3600 + minutes * 60 + seconds

    if total_seconds > currency:
        print("Insufficient balance. Cannot spend more time than available.")
    else:
        time_spent = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        transaction_history.append(f"{time_spent} Spent {hours}h {minutes}m {seconds}s for '{task_description}'")

        currency -= total_seconds
        print(f"Time spent: {hours}h {minutes}m {seconds}s")
        print(f"Current balance: {currency} seconds")


def view_history():
    print("Transaction History:")
    for transaction in transaction_history:
        print(transaction)

    print(f"Remaining balance: {currency} seconds")


def delete_all():
    confirmation = input("Are you sure you want to delete all transactions? (yes/no): ").lower()
    if confirmation == 'yes':
        global transaction_history, currency
        transaction_history = []
        currency = 0
        print("All transactions deleted.")
    else:
        print("Deletion canceled.")


def main():
    load_data_from_file()

    while True:
        print("\nTIMEXEL Options:")
        print("P: Pile time")
        print("S: Spend time")
        print("V: View transaction history")
        print("D: Delete all transactions")
        print("Q: Quit")

        choice = input("Enter your choice (P/S/V/D/Q): ").upper()

        if choice == 'P':
            pile_time()
        elif choice == 'S':
            spend_time()
        elif choice == 'V':
            view_history()
        elif choice == 'D':
            delete_all()
        elif choice == 'Q':
            save_data_to_file()
            print("Quitting TIMEXEL. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter P, S, V, D, or Q.")


if __name__ == "__main__":
    main()
