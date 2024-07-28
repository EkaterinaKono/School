from human import Human
from typing import List
from subject import Subject


class Teacher(Human):
    teachers: dict = {}
    #dict_teachers: dict
    _homeroom_class: "Class"
    _subjects: List[Subject]

    def __init__(self, name, last_name, _subjects, _homeroom_class=None, teachers: dict = {}):
        self.teachers = teachers
        self.name = name
        self.last_name = last_name

        if _homeroom_class:
            self._homeroom_class = _homeroom_class
            Teacher.teachers[str(self._homeroom_class)] = str(self.name) + ' ' + str(self.last_name)
            print(f'{self.name} {self.last_name} является классным руководителем в {self._homeroom_class}')
        else:
            print(f'{self.name} {self.last_name} не является классным руководителем')

        self._subjects = _subjects

    def set_class(self, new_homeroom_class):
        self._homeroom_class = new_homeroom_class
        print('new_homeroom_class = ', self._homeroom_class)

    def get_class(self):
        return f'{self.name} {self.last_name} является классным руководителем в {self._homeroom_class}'

    def __repr__(self):
        return (f'teacher: {self.name} {self.last_name}, subjects: {self._subjects},'
                f' homeroom class: {self._homeroom_class}')

    def __str__(self):
        return (f'{self.name} {self.last_name} is teaching {self._subjects}. {self.name} {self.last_name}'
                f' is classroom teacher of {self._homeroom_class} class')

   # @staticmethod
    #def set_dict_teachers():
        #dict_teachers = Teacher.teachers
        #print(dict_teachers)
        #return dict_teachers
