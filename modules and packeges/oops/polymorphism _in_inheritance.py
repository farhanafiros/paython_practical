class shape:
    def area(self):
        return 0
class circle (shape):
    def area(self):
        return 3.14*5*5

class rectangle(shape):
    def area(self):
        return 10*5

shape = [circle(),rectangle()]
for s in shape:
    print (s.area())


