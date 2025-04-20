class Person:
    number_of_people = 0

    def __init__(self,name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

#p1 = Person("Tim")
#p2 = Person("Jill")

#Person.number_of_people = 9
#print(p2.number_of_people)

people = {1: "Tim", 2: "Jill", 3: "Jane", 4: "Jimmy"}

for key, individual in people.items():
    people[key] = Person(individual)
    print(f"Hi my name's {people[key].name}!", end= " ")
    if key == len(people):
        print(f"\nThere are {Person.number_of_people_()} people in this room.")
