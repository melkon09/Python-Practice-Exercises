class Orders:
    def __init__(self, items):
        self.items = items

    def __add__(self, other):
        return self.items + other.items

    def __gt__(self, other):
        return len(self.items) > len(other.items)

order1= Orders([1,2,3,4,5,6])
order2= Orders([10, 20, 30])

print('Order 1 + order 2=', order1 + order2)