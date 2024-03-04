class Teacher():
    def __init__(self, name, age, salary):
        self.name=name
        self.age=age

        self.__salary = salary

    def show_details    