class Dog:

    def __init__(self,name, age):
        self.name = name
        self.age = age

    #def add_one(self, x):
        #return x + 1

    def bark(self):
        print("bark")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

#d = Dog()
#print(d.add_one(9))
#d.bark()
#print(type(d))

d = Dog("Tim", 12)
d2 = Dog("Bill", 9)
print(d.name)
print(d2.name)
print(d.get_age())
print(d.get_age())
d.set_age(23)
print(d.get_age())
