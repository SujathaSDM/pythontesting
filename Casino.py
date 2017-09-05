import random
class die(object):
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

print( " 6 sides Die")
d = die(6)
print(d.roll())
print(d.roll())
print(d.roll())
d.roll()
d.roll()

print( " 20 sides Die")
d2 = die(20)
print(d2.roll())
print(d2.roll())
print(d2.roll())
d2.roll()
d2.roll()
d2.roll()