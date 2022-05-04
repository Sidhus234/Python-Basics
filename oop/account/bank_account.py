class Account:

    def __init__(self, filepath) -> None:
        self.filepath = filepath
        with open(self.filepath, 'r') as file:
            self.balance = int(file.read())
        pass

    def commit(self):
        with open(self.filepath, "w") as file:
            file.write(str(self.balance))
        pass

    def withdraw(self, amount):
        if self.balance >= amount:
            print("Balance withdrawn successfully")
            self.balance = self.balance - amount
            self.commit()
        else:
            print("Balance not available")
        pass

    def deposit(self, amount):
        self.balance += amount
        self.commit()
        pass


class Checking(Account):

    def __init__(self, filepath, fee) -> None:
        self.fee = fee
        Account.__init__(self, filepath)
        pass

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee
        self.commit()


account = Account("account//balance.txt")
print(account.balance)
account.withdraw(500)
print(account.balance)
account.deposit(350)
print(account.balance)

checking = Checking("account//checking.txt", 2)
checking.deposit(2000)
print(checking.balance)
checking.withdraw(400)
print(checking.balance)
checking.transfer(3500)
print(checking.balance)
