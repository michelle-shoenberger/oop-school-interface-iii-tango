from classes.staff import Staff
from classes.student import Student
import os, csv

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        print('\n')
        for i, student in enumerate(self.students):
            print(f'{i + 1}. {student.name} {student.school_id}')

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                return student

    def add_student(self, student_data):
        student = Student(**student_data)
        self.students.append(student)
        self.save()

    def delete_student(self, id):
        self.students = [s for s in self.students if s.school_id != id]
        self.save()

    def save(self):
        # students
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")

        with open(path, 'w', newline='') as writefile:
            headers = ['name', 'age', 'role', 'school_id', 'password']
            writer = csv.DictWriter(writefile, fieldnames=headers)
            writer.writeheader()
            for student in self.students:
                writer.writerow(vars(student))

        return self.students