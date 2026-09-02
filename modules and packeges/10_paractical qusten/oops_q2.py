from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPIPayment(Payment):

    def pay(self, amount):
        print("Paid", amount, "using UPI")


class CardPayment(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Card")


p1 = UPIPayment()
p2 = CardPayment()

p1.pay(1000)
p2.pay(2000)