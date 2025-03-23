

class Student :
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grades(self, grades):
        for grade in grades:
            self.grades.append(grade)
        
    def average (self):
        average = 0
        for g in self.grades:
           
            average += g


        average_grade = average/len(self.grades)
        return average_grade
    def info(self):
        return f" Student :{self.name}, Age :{self.age}, Average : {int(self.average())}"


student1 = Student("Ali",21)
student1.add_grades([89,100,95,70,65])
print(student1.info())

        