class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    def Attempt_withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds. Current balance:", self.balance)
            return self.balance
        else:
            self.balance -= amount
            return self.balance
bc = BankAccount(1000)
print("Balance after deposit:", bc.deposit(500))
print("Balance after withdrawal:", bc.withdraw(200))
print("Balance after attempt_withdraw:", bc.Attempt_withdraw(2000))