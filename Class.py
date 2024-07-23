import csv
from typing import List
import Student
import Teacher
from Teacher import Teacher
from Student import Student


class Class(list):
    _grade: int
    _letter: str
    _students: List["Student"]
    _homeroom_teacher: "Teacher"

    def __init__(self, grade, letter, homeroom_teacher=None, students=[]):
        super().__init__()
        self._students = []
        self._grade = grade
        self._letter = letter
        for k in Teacher.teachers.keys():
            if (str(self._grade) + self._letter) == k:
                self._homeroom_teacher = Teacher.teachers[k]
        for i, m in Student.studentss.items():
            if (str(self._grade) + self._letter) == m:
                self._students.append(i)
        studs = self._students
        print('Class initialising')

    def __append__(self, new_student):
        super().__append__(new_student)

    def __remove__(self, student):
        super().__remove__(student)

    def __iter__(self):
        return iter(sorted(self._students))

    def __getitem__(self, name):
        for i in self._students:
            if str(name) in i:
                print(i)

    def __repr__(self):
        return (f'class: {self._grade}{self._letter}, classroom teacher: {self._homeroom_teacher},'
                f' students: {self._students}')

    def __str__(self):
        return (f'students of class {self._grade}{self._letter}: {self._students},'
                f' classroom teacher of class {self._grade}{self._letter}: {self._homeroom_teacher}')

    @staticmethod
    def write_csv():
        with open('students.csv', mode='w', encoding='utf-8') as filename:
            file_writer = csv.writer(filename, delimiter='\r', lineterminator='\r')
            file_writer.writerow(['name last_name'])
            file_writer.writerow(Student.studentss)

    @staticmethod
    def read_csv():
        with open('students.csv', newline='') as filename:
            reader = csv.reader(filename)
            for row in reader:
                print(row)
