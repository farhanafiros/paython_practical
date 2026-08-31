class grandfather:
    def grand_father_feature(self):
        print("grandfather:wise and experienced")

class father(grandfather):
    def father_feature(self):
        print("father: hardworking and caring")

class aunt(grandfather):
    def aunt_feature(self):
        print("aunt :kind and supportive")

class child(father,aunt):
    def child_feature(self):
        print("child:energic and curious")

c = child()
c.grand_father_feature()
c.father_feature()
c.aunt_feature()
c.child_feature()
