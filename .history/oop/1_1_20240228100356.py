import math

class Circle():
    def __init__(self, radius):
        self.radius=radius

    def calculate_perimeter(self):
        return 2*math.pi*self.radius
            