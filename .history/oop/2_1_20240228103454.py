from datetime import date

class Person:
    def __init__(self, name, country, dateOfBirth):
        self.name=name
        self.country=country
        self.dateOfBirth=dateOfBirth

    def calculateAge(self):
        today=date.today()
        age=today.year-self.dateOfBirth.year
        if today<date(today.year, self.dateOfBirth.month, self.dateOfBirth.day):
            age-=1
        return age


person1=Person('Meletis', 'Greece', date(1986, 5, 19))
person2=Person('Katerina', 'Greece', date(1992, 8, 27))
person3=Perspn('Eirini- Katerina', 'Greece', date(2022, 10, 18))

l1=[]
l1.append(person1)
l1.append(pers)