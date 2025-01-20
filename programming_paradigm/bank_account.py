class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    #deposit method
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount to deposit must be positive/greater than zero")
        else:
            self.account_balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount to withdraw must be positive/greater than zero")
        if self.account_balance > amount:
            self.account_balance -= amount
            return True
        else:
            return False   
        
    def display_balance(self):
        print(f"Current Balance: ${float(self.account_balance)}")