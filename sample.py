class Bank:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amt):
        self.balance+=amt
    def withdraw(self,amt):
        self.balance-=amt if amt<=self.balance else 0
    def show(self):
        print("Balance:",self.balance)

acc=Bank(5000)
acc.deposit(2000)
acc.withdraw(3000)
acc.show()       
