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
    def __init__(self, name: str, number: int, balance: float) -> None:
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


account1 = Account(name="Daniel", number=235789329, balance=1000)
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
        print(f"In an ordered list, your account(s):")
        for index, account in self.accounts.name:
            print(f"{index} - {account.name}.")


customer1 = CustomerClass(account1)
customer1.get_accounts()

"""
Bank Class: Represents a bank that can have multiple customers.

Methods:

add_customer(customer) – Adds a customer to the bank.
get_customers() – Returns a list of customers in the bank.

Version Updates / Suggested Changes:
Version 1: Add Account Types and Interest Rates

New Feature: Implement different types of accounts (e.g., Checking, Savings) with their own specific behaviors. Savings accounts could have an interest rate, and Checking accounts may have fees for transactions.
Updates:
Modify Account class to inherit from a new AccountType class.
Implement an interest rate in the SavingsAccount subclass and apply it in the deposit() method.
Introduce fees for CheckingAccount transactions (deducted on withdraw()).
Version 2: Transaction History

New Feature: Keep track of all deposits, withdrawals, and account balance changes as a history log.
Updates:
Add a Transaction class to represent a transaction with details like type (deposit/withdrawal), amount, and timestamp.
Add a list of transactions to the Account class, and modify the deposit/withdraw methods to create a new transaction each time.
Implement a get_transaction_history() method in the Account class to view all transactions.
Version 3: Account Security with PIN Verification

New Feature: Add security to accounts by implementing a PIN system. The user must input their PIN to perform any transactions.
Updates:
Add a pin attribute to the Account class.
Create a verify_pin() method to check if the entered PIN matches the stored PIN.
Ensure the deposit() and withdraw() methods ask for PIN verification before proceeding.

"""