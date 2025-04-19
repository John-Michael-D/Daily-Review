class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print("SQUEAK!")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name}, I am {self.age} years old, and I have {self.color} fur :3")

class Dog(Pet):
    def speak(self):
        print("Woof")

class Hamster(Pet):
    pass

p1 = Pet("Sparky", 4)
p1.show()
p1.speak()
p2 = Cat("Whiskers", 3, "Orange")
p2.show()
p2.speak()
p3 = Dog("Amigo", 4)
p3.show()
p3.speak()
p4 = Hamster("George", 2)
p4.show()
p4.speak()