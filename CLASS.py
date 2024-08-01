import csv
from typing import List
from teacher import Teacher
from student import Student
from teacher import teachers
from student import studentss
from common import alphabet


class Class(list):
    _grade: int
    _letter: str
    _students: List["Student"]
    _homeroom_teacher: "Teacher"

    def __init__(self, grade: int, letter: str, _homeroom_teacher=None, _students=[]):
        self._students = []
        self._homeroom_teacher = None
        if grade in range(1, 12):
            self._grade = grade
        else:
            raise AttributeError("Номер класса должен быть от 1 до 11!")
        if letter in alphabet:
            self._letter = letter
        else:
            raise AttributeError("Буквой класса должна быть заглавная буква из русского алфавита!")
        for k in teachers.keys():
            if (str(self._grade) + self._letter) == k:
                self._homeroom_teacher = teachers[k]
        for i, m in studentss.items():
            if (str(self._grade) + self._letter) == m:
                self._students.append(i)

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
        return (f'Класс: {self._grade}{self._letter}, классный руководитель: {self._homeroom_teacher},'
                f' ученики: {self._students}')

    def __str__(self):
        return (f'Ученики класса {self._grade}{self._letter}: {self._students},'
                f' классный руководитель класса {self._grade}{self._letter}: {self._homeroom_teacher}')

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
