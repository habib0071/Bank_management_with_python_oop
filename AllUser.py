from Information_of_bank import *

class Person:
    def __init__(self, name, email, address, phone) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.information = Information()

class User(Person):
    def __init__(self, name, email, address, phone, initial_balance) -> None:
        super().__init__(name, email, address, phone)
        self.initial_balance = initial_balance
        self.loan = None
        self.history = []
        self.my_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.initial_balance += amount
            self.my_balance += amount
            str = f"Deposited ${amount}"
            self.history.append(str)
        else:
            print('You have to give some money for deposit')

    def withdraw(self, amount):
        if 0 < amount <= self.information.max_withdraw and self.information.min_withdraw <= amount <= self.initial_balance:
            self.initial_balance -= amount
            self.my_balance -= amount
            str = f"Withdraw ${amount}"
            self.history.append(str)
        else:
            print('Invalid withdrawal amount or insufficient funds.')
    

    def see_history(self):
        print(f'Name : {self.name}')
        print()
        print("History:")
        for his in self.history:
            print(his)

    def check_balance(self):
        print(f'hey! {self.name}. Your balanace is : {self.my_balance}')  


    def transfer(self, recipient, amount):
        if 0 < amount <= self.initial_balance:
            self.initial_balance -= amount
            for key, value in self.information.List_of_user.items():
                if key == recipient:
                    value.initial_balance += amount

class Employee(Person):
    def __init__(self, name, email, address, phone, type_of_work) -> None:
        super().__init__(name, email, address, phone)
        self.type_of_work = type_of_work

