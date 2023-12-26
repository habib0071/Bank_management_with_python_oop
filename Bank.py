from AllUser import *
from Information_of_bank import *

class Bank:
    def __init__(self, name, address, phone, email) -> None:
        self.name = name 
        self.address = address
        self.phone = phone
        self.email = email
        self.information = Information()
        
    def create_user(self, name, email, address, phone, initial_balanc):
        user = User(name, email, address, phone, initial_balanc)
        self.information.List_of_user[name] = user
    
    def create_employee(self, name, email, address, phone, type_of_work):
        employee = Employee(name, email, address, phone, type_of_work)
        self.information.List_of_employee[name] = employee