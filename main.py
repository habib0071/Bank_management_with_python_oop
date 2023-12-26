from Bank import *
from AllUser import *

def main():
    
    dhaka_bank = Bank("dhaka_bank", "rongpur brance", "123-4567-0098", "dhakabankrongpur@bank.com")
    info = dhaka_bank.information
    dhaka_bank.create_user("rafid", "rafid@gamil.com", "Miragonj", '017774547771', 100)
    rafids_bank_id = info.List_of_user.get('rafid')
    dhaka_bank.create_user("habib", "habib@gamil.com", "Borobag", '017774543471', 200)
    habib_bank_id = info.List_of_user.get('habib')

    info.see_user()


    rafids_bank_id.deposit(50)
    # rafids_bank_id.deposit(10)
    # rafids_bank_id.deposit(10)
    rafids_bank_id.withdraw(20)

    #rafids_bank_id.see_history()

    habib_bank_id.deposit(30)
    # habib_bank_id.deposit(10)
    # habib_bank_id.deposit(50)
    habib_bank_id.withdraw(40)

    habib_bank_id.see_history()


    # rafids_bank_id.deposit(10)
    # habib_bank_id.withdraw(20)
    
    #habib_bank_id.see_history()
    rafids_bank_id.see_history()

    print()
    print(info.see_bank_amount())

if __name__ == '__main__':
    main()