"""
Task: Design a Simple Banking System
You are tasked with creating an object-oriented banking system with the following classes and functionality:

Account Class: Represents a bank account with:
Account holder’s name
Account number
Account balance
"""


# Initialize the Account CLass
class Account:
    def __init__(self, name: str, number: str, balance: float) -> None:
        self.name = name
        self.number = number
        self.balance = balance

    # Methods:
    # Deposit – Adds the amount to the balance.
    def deposit(self, amount: float):
        self.balance += amount
        return self.balance

    # Withdraw – Deducts the amount from the balance (if sufficient funds are available).
    def withdraw(self, amount: float):
        if amount <= self.balance:
            print(f"Withdraw successful!")
            self.balance -= amount
            return self.balance
        else:
            print("Insufficient funds")
            print(f"You need an extra {amount-self.balance} to withdraw that!")
            return self.balance

    # Get balance - Returns the current balance.
    def get_balance(self):
        print("----------------------------------")
        print(f"Hello {self.name}!")
        print(f"Your balance is ${self.balance}")
        print("Thank you for banking with us!")
        print("----------------------------------")
        return self.balance

    # __str__() – Returns a string representation of the account details.
    def __str__(self):
        return f"Hello {self.name}, your number is {self.number} and your balance is ${self.balance}"


account1 = Account(name="Daniel", number="235789329", balance=1000)
# Testing
# print(account1.name)
# print()
# account1.withdraw(2000)
# print()
# print(account1.balance)
# print()
# account1.deposit(500)
# print()
# account1.__str__()
# print()
# account1.get_balance()
account2 = Account("Gabriel", "0893847083", 7000)


# Customer Class: Represents a bank customer who can have multiple accounts.
class CustomerClass:
    def __init__(self, account):
        self.account = account
        self.accounts = [self.account.__str__()]

    # Add account – Adds an account to the customer
    def add_account(self, account):
        self.accounts.append(account)

    # () – Returns a list of accounts owned by the customer.
    def get_accounts(self):
        print(self.accounts)
        print("-------------")


customer1 = CustomerClass(account1)
customer1.get_accounts()
