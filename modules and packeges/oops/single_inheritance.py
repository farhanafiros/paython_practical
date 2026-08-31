class animal:
    def eat (self):
        print("EATING...")

class dog(animal):
    def bark(self):
        print ("barking....")
a = dog()      
a.eat()
a.bark()
