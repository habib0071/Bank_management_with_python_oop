class Information:
    def __init__(self) -> None:
        self.List_of_user = {}
        self.List_of_employee = {}
        self.total_amount_of_bank = 0
        self.total_loan = 0
        self.lsit_of_loan_with_user = {}
        self.max_withdraw = 50
        self.min_withdraw = 10

    def see_user(self):
        for key, value in self.List_of_user.items():
            print(f'Name    : {key}')
            print(f'Email   : {value.email}')
            print(f'Address : {value.address}')
            print(f'Phone   : {value.phone}')
            print(f'Balance : {value.initial_balance}')
            print()
    
    def see_total_bank_balance(self):
        total_balance = sum(user.initial_balance for user in self.List_of_user.values())
        self.total_amount_of_bank = total_balance
        print(f'The Total amount of bank {total_balance}')
    
