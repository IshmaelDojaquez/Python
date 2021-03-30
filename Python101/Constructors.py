
class Point:
    def __init__(self, x, y):  # constructor gets called at the time of creation of the object
        self.x = x  # uses self references  the current object
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
point.x = 11  # you can change the constructor value
print(point.x)

# Practice


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John")
john.talk()

bob = Person("Bob")
bob.talk()
