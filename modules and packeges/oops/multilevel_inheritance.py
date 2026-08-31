class Grandparent:
    def feature_grandparent(self):
        print("grandparent feature")

class parent(Grandparent):
    def feature_parent(self):
        print("parent feature")

class child(parent):
    def feature_child(self):
        print("child feature")

c = child()
c.feature_grandparent()
c.feature_parent()
c.feature_child()
