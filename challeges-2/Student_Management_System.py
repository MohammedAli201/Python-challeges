"This is challeges that will enforces you to use what you have learned"

class Student: 
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades if grades is not None else []

        self.attendance =0
    def add_grade(self,grade):
        for gr in grade:
            self.grades.append(gr)
    def mark_attendence(self):
        self.attendance +=1
        return f"{self.name}'s atttendance marked. total:  {self.attendance} days"
    def get_average(self):
        average = 0
        for grade in self.grades:
            average += grade
        return average / len(self.grades)

    
    def info(self):
        avg = self.get_average()
        return f"{self.name} | Grades: {self.grades} | Avg: {avg:.2f} | Attendance: {self.attendance} days"



student = Student("Ali")
student.add_grade([80, 90, 100])
student.mark_attendence()

print(student.info())

        