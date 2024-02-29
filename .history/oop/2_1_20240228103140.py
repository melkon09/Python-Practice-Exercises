from datetime import date

class Person:
    def __init__(self, name, country, dateOfBirth):
        self.name=name
        self.country=country
        self.dateOfBirth=dateOfBirth

    def calculateAge(self):
        today=date.today()
        age=today.year-self.dateOfBirth.year
        if today<date()    