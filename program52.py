class BankAccount:

    # Constructor
    def __init__(self, account_number, name, account_type, balance):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited:", amount)
            print("Current balance:", self.balance)
        else:
            print("Invalid amount")

    # Withdraw method
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
            print("Current balance:", self.balance)
        else:
            print("Insufficient balance or invalid amount")

    # Display method
    def display(self):
        print("\n--- Account Details ---")
        print("Account Number:", self.account_number)
        print("Name:", self.name)
        print("Account Type:", self.account_type)
        print("Balance:", self.balance)


# Getting user input
acc_no = int(input("Enter account number: "))
name = input("Enter name: ")
acc_type = input("Enter account type: ")
balance = float(input("Enter initial balance: "))

# Creating object
b = BankAccount(acc_no, name, acc_type, balance)

b.display()

# Deposit
amount = float(input("\nEnter amount to deposit: "))
b.deposit(amount)

# Withdraw
amount = float(input("\nEnter amount to withdraw: "))
b.withdraw(amount)

# Display final balance
print("\nFinal Balance:", b.balance)

