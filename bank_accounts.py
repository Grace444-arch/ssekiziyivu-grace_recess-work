#real world  scenarios or problems
#bank accounts: saving account and current account inherit from bank account
#deposit, withdraw, display balance, types of accounts

class BankAccount:
    def _init_(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    def withdraw(self, amount):
        self.balance -= amount
        print(f"withdraw {amount}. New balance: {self.balance}")