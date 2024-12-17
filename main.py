# Python Banking Program

def show_balance(balance):             #function to show balance off customer
    print(40 * "*")
    print(f"Your balance is ${balance: .2f}")
    print(40 * "*")
    pass


def deposit():                  #function to make deposit
    print(40 * "*")
    amount = float(input("Enter an amount to be deposited: "))
    print(40 * "*")
    if amount < 0:
        print(40 * "*")
        print("Invalid amount please select a value greater than 0")
        print(40 * "*")
        return 0
    else:
        return amount

def withdraw(balance):                 #function to make withdraws
    print(40 * "*")
    amount = float(input("Enter an amount to be withdrawn: "))
    print(40 * "*")
    if amount > balance:
        print(40 * "*")
        print("Insufficient funds")
        print(40 * "*")
        return 0
    elif amount < 0:
        print(40 * "*")
        print("Amount must be greater than 0")
        print(40 * "*")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print(40 * "*")
        print("         Banking Program")
        print(40 * "*")

        print("1. Show Balance")
        print("2. Make Deposit")
        print("3. Make a Withdraw")
        print("4. Exit")
        print(40 * "*")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print(40 * "*")
            print("Invalid input! Please choose a number (1-4)")
            print(40 * "*")
    print(40 * "*")
    print("Thank you for banking with us! Have a nice day!")

if __name__ == '__main__':
    main()

