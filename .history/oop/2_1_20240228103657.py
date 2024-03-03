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

i=0
for person in [person1, person2, person3]:
    i+=1
    print(f'Person {i}:')
    print(f'Name: {person.name}')
    print(f'Country: {person.country}')
    print(f'DoB: {person.dateOfBirth}')
    print(f'Age: ')