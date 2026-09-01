class BankAccont:
    def __init__(self,balance):
        self.__balance =balance 

acc = BankAccont(1000)  
print(acc.__balance)
acc.balance = 500 
print(acc.__balance)