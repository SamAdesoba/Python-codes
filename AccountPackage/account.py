class Account:

    def __init__(self,  name: str, password: str, phone_number: str):
        self.balance = 0
        self.name = name
        self.password = password
        self.phone_number = phone_number

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.balance += amount

    def withdraw(self, amount: int, password: str):
        if password is not self.password:
            raise ValueError("Your password is wrong")
        if password is self.password:
            if amount < 0:
                raise ValueError("Amount cannot be negative")
            if amount > self.balance:
                raise ValueError("Can't withdraw more than the available")
            self.balance -= amount

    def load_airtime(self, amount, phone_number):
        if phone_number is self.phone_number:
            if amount < 0:
                raise ValueError("Amount cannot be negative")
            if amount > self.balance:
                raise ValueError("Can't load more than the available")
            self.balance -= amount

    def transfer(self, receiver_account, amount: int, password: str):
        self.withdraw(amount, password)
        receiver_account.deposit(amount)
