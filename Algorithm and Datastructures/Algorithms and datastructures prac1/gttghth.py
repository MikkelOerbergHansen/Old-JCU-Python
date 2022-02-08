

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


My_Name = str(input("input your name: "))
My_age = int(input("input your age: "))

person = Person(
    My_Name,
    My_age
)

print(person.name, person.age)

