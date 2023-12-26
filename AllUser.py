from Information_of_bank import *

class Person:
    def __init__(self, name, email, address, phone) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.information = Information()

class User(Person):
    def __init__(self, name, email, address, phone, initial_blance) -> None:
        super().__init__(name, email, address, phone)
        self.__initial_balance = initial_blance
        self.information.total_amount_of_bank += initial_blance
        self.loan = None
        self.history = []

    def deposit(self, amount):
        if amount > 0:
            self.__initial_balance += amount
            self.information.total_amount_of_bank += amount
            str = f"Deposited ${amount}"
            self.history.append(str)
            print(f"Deposited ${amount}. New balance: ${self.__initial_balance}")
            print("The : ",self.information.total_amount_of_bank)

        else:
            print('You have to give some money for deposit')

    def withdraw(self, amount):
        if 0 < amount <= self.information.max_withdraw and self.information.min_withdraw <= amount <= self.__initial_balance:
            self.__initial_balance -= amount
            self.information.total_amount_of_bank -= amount
            str = f"Withdraw ${amount}"
            self.history.append(str)
            print(f"Withdraw ${amount}. New balance: ${self.__initial_balance}")
            print("The : ",self.information.total_amount_of_bank)
        else:
            print('Invalid withdrawal amount or insufficient funds.')

    def see_history(self):
        print(self.name)
        print(self.history)

            
class Employee(Person):
    def __init__(self, name, email, address, phone, type_of_work) -> None:
        super().__init__(name, email, address, phone)
        self.type_of_work = type_of_work
