class dog:
    def speak(self):
        return "woof!"
class cat:
    def speak(self):
        return "meow!"

def animal_sound(animal):
    print(animal.speak())

d = dog()
c = cat()

animal_sound(d)
animal_sound(c)