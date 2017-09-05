class Greeter(object):
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello "+ self.name)

    def goodbye(self):
        print("Godbye " + self.name)


g = Greeter("Srinikesk")
g.hello()
g.goodbye()

g2 = Greeter("Ananya")
g2.hello()
g2.goodbye()

