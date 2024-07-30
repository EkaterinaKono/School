import csv
from typing import List
from teacher import Teacher
from student import Student
from teacher import teachers
from student import studentss


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
        for k in teachers.keys():
            if (str(self._grade) + self._letter) == k:
                self._homeroom_teacher = teachers[k]
        for i, m in studentss.items():
            if (str(self._grade) + self._letter) == m:
                self._students.append(i)
        print('Class initialising')

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
        super().append(new_student)

    def __remove__(self, student):
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

    def write_csv(self, filename: str):
        with open(filename, mode="w", encoding="utf8") as filename:
            file_writer = csv.writer(filename, delimiter='\r', lineterminator='\r')
            file_writer.writerow([f"Класс: {self._grade} {self._letter}"])
            file_writer.writerow([f"Классный руководитель: {self._homeroom_teacher}"])
            file_writer.writerow([" "])
            file_writer.writerow(["Имя Фамилия"])
            file_writer.writerow(self)

    @staticmethod
    def read_csv(filename: str):
        with open(filename, "r", encoding="utf8") as filename:
            reader = csv.reader(filename)
            for row in reader:
                print(row)
