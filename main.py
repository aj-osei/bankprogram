# Python Banking Program

def show_balance():             #function to show balance off customer
    pass


def deposit():                  #function to make deposit
    pass

def withdraw():                 #function to make withdraws
    pass


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
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        is_running = false
    else:
        print("Invalid input! Please choose a number (1-4)")

