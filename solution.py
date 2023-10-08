# Global variable
account_balance = 100

# Function to check the current balance
def check_balance():
    global account_balance
    print(f"Your current balance is ${account_balance}.")
    return account_balance
# Function to deposit an amount
def deposit(amount):
    global account_balance
    account_balance += amount
    print(f"You deposited ${amount}. New balance is ${account_balance}.")

# Function to withdraw an amount
def withdraw(amount):
    global account_balance
    if amount > account_balance:
        print("Insufficient funds!")
    else:
        account_balance -= amount
        print(f"You withdrew ${amount}. New balance is ${account_balance}.")

# Main program loop
while True:
    # Display menu
    print("\nChoose an option:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = input("> ")
    
    if choice == "1":
        check_balance()
    elif choice == "2":
        amount = float(input("Enter the amount to deposit: "))
        deposit(amount)
    elif choice == "3":
        amount = float(input("Enter the amount to withdraw: "))
        withdraw(amount)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


# testing 

