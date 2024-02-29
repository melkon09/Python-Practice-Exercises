import math

class Calculator():
    def add(self, x, y):
        return x+y

    def subtract(self, x, y):
        return x-y

    def multiply(self, x, y):
        return x*y

    def divide(self, x, y):
        if y:
            return x/y
        else:
            return ('Cannot divide by zero.')

calculator = Calculator()

result=calculator.add(5,4)
print('5 + 4 = ',result)

result=calculator.subtract(20, 7)
print('20 - 7 = ', result)

result=calculator.multiply(5, 7)
print('5 * 7 = ',result)

result=calculator.divide(10, 0)
print('10 / 0 = ',result)

result=calculator.divide(30, 5)
print('30 / 5 = ',result)