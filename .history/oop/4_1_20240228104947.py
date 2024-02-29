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
        return 2*