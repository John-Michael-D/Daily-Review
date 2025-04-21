import math

class Math:

    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print("Run")

print(Math.add5(50))
print(Math.add10(55))
Math.pr()