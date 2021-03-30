class Point:  # capitalize the first letter of each word when creating classes
    def move(self):
        print("move")

    def draw(self):
        print("draw")



point1 = Point()
point1.x = 10
point1.y = 20  # attributes
print(point1.x)
point1.draw()

point2 = Point()  # creates its own instance of the class Point
point2.x = 1
print(point2.x)

