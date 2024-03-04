class Orders:
    def __init__(self, items):
        self.items = items

    def __add__(self, other):
        return self.items + other.items

    def __gt__(self, other):
        return         