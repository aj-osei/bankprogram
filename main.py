# Python Banking Program

def show_balance():             #function to show balance off customer
    print(f"Your balance is ${balance: .2f}")
    pass


def deposit():                  #function to make deposit
    amount = float(input("Enter an amount to be deposited: "))
    if amount < 0:
        print("Invalid amount please select a value greater than 0")
        return 0
    else:
        return amount

def withdraw():                 #function to make withdraws
    amount = float(input("Enter an amount to be withdrawn: "))
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
    else:
        return amount


balance = 0
is_running = True

while is_running:
    print("Banking Program")
    print("1. Show Balance")
    print("2. Make Deposit")
    print("3. Make a Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        show_balance()
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        balance -= withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("Invalid input! Please choose a number (1-4)")


print("Thank you for banking with us! Have a nice day!")

