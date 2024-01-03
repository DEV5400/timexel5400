# TIMEXEL - Time as Currency Management

TIMEXEL is a simple Python-based application that treats time as a form of currency. Users can perform various operations such as piling time, spending time, viewing transaction history, deleting all transactions, and quitting the program.

## Features

1. **PILE (P):**
   - Add time to your currency balance.
   - Enter task description and the number of hours, minutes, and seconds.
   - Records the transaction, updating the total currency balance.

2. **SPEND (S):**
   - Spend time from your currency balance.
   - Enter task description and the number of hours, minutes, and seconds.
   - Checks if there is sufficient currency and updates the total currency balance.
   - Records the transaction.

3. **VIEW (V):**
   - Displays a transaction history, including date, time, task, and the amount of time added or spent.
   - Added amounts are displayed with a '+' sign, and spent amounts with a '-' sign.
   - Shows the remaining total balance.

4. **DELETE ALL (D):**
   - Delete the entire transaction history.
   - Prompts for confirmation before proceeding with deletion.

5. **QUIT (Q):**
   - Save the current transaction history to a file named "transaction_history.json".
   - Exits the TIMEXEL program.

## Usage

1. Run the TIMEXEL program.
2. Choose options (P/S/V/D/Q) to perform specific operations.
3. Follow the prompts to enter task details and time.
4. View transaction history to keep track of your time transactions.
5. Quit the program to save data and exit.

## Persistence

- The program utilizes a global variable `currency` to keep track of the total time balance.
- The transaction history is stored in a list named `transaction_history`.
- Data is read from and written to a JSON file ("transaction_history.json") for persistence across program runs.

## Usage Example

```plaintext
TIMEXEL Options:
P: Pile time
S: Spend time
V: View transaction history
D: Delete all transactions
Q: Quit

Enter your choice (P/S/V/D/Q): P
Enter task description: Coding
Enter hours: 2
Enter minutes: 30
Enter seconds: 0
Time added: 2h 30m 0s
Current balance: 9000 seconds

...

