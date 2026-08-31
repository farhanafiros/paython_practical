class mother :
    def cook(self):
        print("cooking....")

class father:
    def driver(self):
        print("driving...")

class child(mother,father):
    pass

c = child()
c.cook()
c.driver()
