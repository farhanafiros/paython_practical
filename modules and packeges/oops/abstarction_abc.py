from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class UPI(payment):
    def pay(self,amound):
        print("paid",amound,"using upi")

class card(payment):
    def pay(self,amount):
        print("paid",amount,"using card")

p1 = UPI()
p2 = card()

p1.pay(3000)
p2.pay(1000)