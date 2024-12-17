Banking Program Report

What Is This Program?
This program is like a simple bank account system. It lets you:

-Check your balance
-Deposit money into your account
-Withdraw money from your account
-Exit the program
It makes sure you don’t do anything like deposit a negative number or withdraw more money than you have. The program uses basic choices that you can select, and it updates the balance based on what you do.

What Does Each Part Do?
show_balance(balance):
This shows you how much money you have in your account. It takes your balance and prints it out in a simple way.

deposit():
This part lets you put money into your account. It asks you how much you want to deposit, and if you enter a positive number, it adds that amount to your balance. If you enter something wrong, like a negative number, it tells you to try again.

withdraw(balance):
This is for taking money out of your account. It asks how much you want to withdraw, and if you try to take out more money than you have, it gives you an error. It only lets you withdraw if you have enough money and the amount is positive.

main():
This is where the program runs. It lets you choose what you want to do:

See your balance (Option 1)
Deposit money (Option 2)
Withdraw money (Option 3)
Exit the program (Option 4)
The program will keep asking you for input until you choose to exit. It updates the balance whenever you deposit or withdraw.

What Was Hard?
Input Checking: One challenge was making sure the user couldn’t enter bad values, like negative numbers. I had to check if the input was valid and ask again if it wasn’t.
Keeping the Balance Correct: It was important to make sure that the balance updated correctly whenever money was added or taken out. I did this by passing the balance around to different parts of the program.

Ideas for Improving It
Saving the Balance: Right now, the balance only exists while the program is running. It would be cool to save the balance to a file so it’s remembered the next time you open the program.
More Accounts: This program only has one account, but it could be expanded to allow multiple users to have different accounts.
Better Design: It’s a simple text-based program, but a graphical user interface (GUI) would make it look nicer and be easier to use.
