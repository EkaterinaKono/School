import csv
from typing import List
from teacher import Teacher
from student import Student


class Class(list):
    _grade: int
    _letter: str
    _students: List["Student"]
    _homeroom_teacher: "Teacher"

    def __init__(self, grade, letter, _homeroom_teacher=None, _students=[]):
        self._students = []
        self._homeroom_teacher = None
        self._grade = grade
        self._letter = letter
        print(Teacher.teachers)       # выводит пустой словарь
        for k in Teacher.teachers.keys():
            if (str(self._grade) + self._letter) == k:
                self._homeroom_teacher = Teacher.teachers[k]
        for i, m in Student.studentss.items():
            if (str(self._grade) + self._letter) == m:
                self._students.append(i)
        print('Class initialising')
        print(self._homeroom_teacher)     # выводит None
        print(Teacher.teachers)     # выводит пустой словарь

    ''''@property
    def _grade(self):
        return self._grade

    @_grade.setter
    def _grade(self, new_grade):
        self._grade = new_grade

    @property
    def _letter(self):
        return self._letter

    @_letter.setter
    def _letter(self, new_letter):
        self._letter = new_letter'''

    def __append__(self, new_student):
        #super().__append__(new_student)
        super().append(new_student)

    def __remove__(self, student):
        #super().__remove__(student)
        super().remove(student)

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
        # метод __str__ не выводит студентов и преподавателя

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
