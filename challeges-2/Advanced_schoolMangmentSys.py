""" This is more advanced: we should build system to manage multiple students, teachers and courses """
import random
class Student:
    def __init__(self,name, id,grades=None):
        self.name =name
        self.id = id
        self.attendance =0
        self.grades = grades if grades is not None else {}
        

    def add_grade(self, course, grade):
            if course in self.grades:
                self.grades[course].append(grade)
            else:
                self.grades[course] = [grade]
    def get_average(self):
        total = 0
        count = 0
        for grades in self.grades.values():
            total += sum(grades)
            count += len(grades)
        return total / count if count else 0

    def mark_attendance(self):
        self.attendance += 1
        return f"{self.name} is marked . Total : {self.attendance} days"
    
class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students_enrolled = []

    def enroll_student(self, student):
        self.students_enrolled.append(student)
        return f"{student.name} is enrolled in {self.name}"

    def list_students(self):
        return [s.name for s in self.students_enrolled]

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def assign_grade(self, student, course, grade):
        student.add_grade(course, grade)
        return f"{self.name} assigned grade {grade} to {student.name} for {course}"




# Create teacher
teacher1 = Teacher("Mr. Smith", "Math")

# Create courses
course_math = Course("Mathematics", teacher1)
course_sci = Course("Science", Teacher("Ms. Jane", "Science"))

# Create students
student1 = Student("Ali", 101)
student2 = Student("Lina", 102)
student3 = Student("John", 103)

# Enroll students
print(course_math.enroll_student(student1))
print(course_math.enroll_student(student2))
print(course_sci.enroll_student(student3))

# Mark attendance
print(student1.mark_attendance())
print(student2.mark_attendance())

# Assign grades
print(teacher1.assign_grade(student1, "Mathematics", random.randint(70, 100)))
print(teacher1.assign_grade(student1, "Mathematics", random.randint(70, 100)))
print(teacher1.assign_grade(student2, "Mathematics", random.randint(70, 100)))

# Show student grades and average
for student in [student1, student2]:
    print(f"{student.name}'s grades: {student.grades}")
    print(f"{student.name}'s average: {student.get_average():.2f}")

# List students in Math course
print("Students in Mathematics:", course_math.list_students())

