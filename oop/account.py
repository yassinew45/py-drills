from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        self.balance += amount

    @abstractmethod
    def withdraw(self, amount):
        pass

    def __repr__(self):
        return f"{type(self).__name__}(owner=\'{self.owner}\', balance={self.balance})"

    def __eq__(self, other):
        if type(other) != type(self):
            return NotImplemented
        else:
            return self.owner == other.owner and self.balance == other.balance

    def __hash__(self):
        return hash((self.owner, self.balance))   # same fields as __eq__, so equal objects hash the same


class SavingsAccount(Account):

    def __init__(self, owner, interest_rate):
        super().__init__(owner)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if amount > self.balance or amount <= 0:
            raise ValueError("amount must be positive and less than the balance")
        self.balance -= amount

    def add_interest(self):
        self.balance = self.balance * (1 + self.interest_rate)


