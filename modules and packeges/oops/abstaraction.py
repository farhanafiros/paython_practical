from abc import ABC,mabstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class dog(Animal):
    def sound(self):
        return "bow!"
class cat(Animal):
    def sound(self):
        return "meow"

D = dog()
c = cat()
print(D.sound())
print(c.sound())
    