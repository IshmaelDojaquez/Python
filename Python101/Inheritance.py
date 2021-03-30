# DRY = Dont Repeat Yourself

class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):  # Inheriting from mammal. inside the parenthesis
    def bark(self):
        print("Bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")


class Hamster(Mammal):
    pass  # Python likes to have functions defined in a class. Using pass will allow for no functions


dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.be_annoying()
