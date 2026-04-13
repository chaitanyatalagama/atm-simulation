#ATM simulation using Python
def login(account):
    attempts = 3
    while attempts > 0:
        pin = input("Enter your PIN: ")
        if pin == account["pin"]:
            print("Login successful!\n")
            return True
        else:
            attempts -= 1
            print(f"Wrong PIN! Attempts left: {attempts}")
    print("Too many failed attempts. Exiting...") #if attempts greater than 3
    return False


def check_balance(account):
    print(f"\nCurrent Balance: ₹{account['balance']}")


def deposit(account):
    try:
        amount = float(input("Enter amount to deposit: ₹"))
        if amount > 0:
            account["balance"] += amount
            account["history"].append(f"Deposited ₹{amount}")
            print("Deposit successful!")
        else:
            print("Invalid amount!")
    except ValueError:
        print("Enter a valid number!") #if values other than numbers are given as input


def withdraw(account, limit=5000):
    try:
        amount = float(input("Enter amount to withdraw: ₹"))
        
        if amount <= 0:
            print("Invalid amount!")
        
        elif amount > limit:
            print(f"Withdrawal limit exceeded! Max allowed: ₹{limit}")
        
        elif amount > account["balance"]:
            print("Insufficient balance!")
        
        else:
            account["balance"] -= amount
            account["history"].append(f"Withdrew ₹{amount}")
            print("Withdrawal successful!")
    
    except ValueError:
        print("Enter a valid number!")


def show_history(account):
    print("\nTransaction History:")
    if not account["history"]: #Checks if the history list is empty(is yes prints the statement)
        print("No transactions yet.")
    else:
        for i, txn in enumerate(account["history"], 1):
            print(f"{i}. {txn}")


def atm():
    # Single account
    account = {
        "pin": "0219",
        "balance": 1000,
        "history": []
    }

    if not login(account):
        return

    while True:
        print("\n====== ATM MENU ======")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '1':
            check_balance(account)

        elif choice == '2':
            deposit(account)

        elif choice == '3':
            withdraw(account)

        elif choice == '4':
            show_history(account)

        elif choice == '5':
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid choice!")


# Run program
atm()
