# bankprogram

Python Banking Program
This is a simple command-line banking program written in Python that allows users to perform basic banking operations such as checking their balance, depositing money, and withdrawing funds. It simulates a basic banking interface using a menu-driven approach.

Features:
- Check Balance: View your current account balance.
- Deposit Funds: Add funds to your account.
- Withdraw Funds: Withdraw money from your account.
- Exit: Exit the program.


How It Works:

Check Balance:
Displays the current balance in the account.

Deposit:
Allows the user to enter a positive amount to deposit. If the amount is invalid (negative or zero), the program prompts the user to enter a valid amount.

Withdraw:
Prompts the user to enter the amount they wish to withdraw. If the user attempts to withdraw more than their current balance, the program will notify them of insufficient funds. The program ensures that the withdrawal amount is positive.

Exit:
Ends the program with a friendly exit message.

Future Improvements
-Implement user authentication (login/signup system).
-Save user data (balance, transaction history) between sessions using a file/database.
-Add a transaction history feature to track deposits and withdrawals.
