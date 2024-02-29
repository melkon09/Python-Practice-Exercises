import math

class Shape():
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius

    def calculate_area(self):
        return math.pi*self.radius**2

    def calculate_perimeter(self):
        return 2*math.pi*radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length=length
        self.width=width

    def calculate_area(self):
        return length*width

    def calculate_perimeter(self):
        return 2*(length+width)

class Triangle(Shape):
    def __init        