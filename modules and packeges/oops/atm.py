from abc import ABC ,abstractmethod

class ATM(ABC):
    @abstractmethod
    def withdraw(self):
        pass
class mybankATM(ATM):
    def withdraw(self):
        self.__verify_pin()
        self.__check_balance()
        self.__update_server()
        print("cash withdraw successfully")


    def __verify_pin(self):
        print("pin verified")

    def __check_balance(self):
        print("Balance checked")

    def __update_server(self):
        print("server_update")

ATM =mybankATM()
ATM.withdraw()