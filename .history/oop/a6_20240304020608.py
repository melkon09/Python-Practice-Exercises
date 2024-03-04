class Teacher():
    def __init__(self, name, age, salary):
        self.name=name
        self.age=age

        self.__salary = salary

    def show_details(self):
        print('Name: ', self.name)
        print('Age: ', self.age)

        print('Salary: ', self.__salary)

teacher = Teacher('Raj', 45, 25000)

teacher