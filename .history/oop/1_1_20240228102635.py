import math

class Circle():
    def __init__(self, radius):
        self.radius=radius

    def calculate_perimeter(self):
        return 2*math.pi*self.radius

    def calculate_area(self):
        return math.pi*self.radius**2

radius= float(input('Give me a radius: '))

circ1=Circle(radius)

area=circ1.calculate_area()
print(f'Area of circle: {area:.3f}')