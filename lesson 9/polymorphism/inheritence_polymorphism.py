import math


class Shape:
    def area(selfself):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rect(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

class Triangle(Shape):
    def __int__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height




circle = Circle(5)
print("Area of the circle:", circle.area())


rectangle = Rect(4, 6)
print("Area of the rectangle:", rectangle.area())

triangle = Triangle(4, 8)
print("Area of the triangle:", triangle.area())

