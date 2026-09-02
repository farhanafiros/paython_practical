from abc import ABC,abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start(self,brand,model):
        pass
class car(vehicle):
    def start(self):
        print("toyota,fortuner")
        print("car start with a button")

class bike(vehicle):
    def start(self):
        print("royal Enified,GT")
        print("bike start with a key")

c = car()  
d = bike()  

c.start()
d.start()