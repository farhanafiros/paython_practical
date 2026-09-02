
class mybankATM:
    def withdraw(self):
        print("cash withdraw successfully")


    def verify_pin(self):
        print("pin verified")

    def check_balance(self):
        print("Balance checked")

    def update_server(self):
        print("server_update")

atm =mybankATM()
atm.verify_pin()
atm.check_balance()
atm.update_server()
atm.withdraw()