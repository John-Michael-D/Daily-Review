class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade #0% through 100%
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            return False
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

s1 = Student("Tim", 20, 99)
s2 = Student("Mark", 21, 76)
s3 = Student("Jane", 24, 85)

c1 = Course("Math", 25)
c1.add_student(s1)
c1.add_student(s2)
c1.add_student(s3)
print(c1.students[0].name)
print(c1.students[1].name)
print(c1.students[2].name)
print(c1.get_average_grade())