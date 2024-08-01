from human import Human
from typing import List
from subject import Subject
from common import teachers
from common import alphabet


class Teacher(Human):
    _homeroom_class: "Class"
    _subjects: List[Subject]

    def __init__(self, name: str, last_name: str, subjects, homeroom_class: "Class" = None):
        i = 0
        self.name = name
        self.last_name = last_name

        if homeroom_class:
            for ch in homeroom_class:
                i += 1
            if i < 2 or i > 3:
                raise AttributeError("Школьный класс должен содержать цифру от 1 до 11"
                                     " и заглавную букву русского алфавита!")
            elif i == 3:
                if homeroom_class[i - 1] in alphabet:
                    if homeroom_class[0].isdigit() and homeroom_class[1].isdigit():
                        if int(str(homeroom_class[0]) + str(homeroom_class[1])) in range(1, 12):
                            self._homeroom_class = homeroom_class
                        else:
                            raise AttributeError("Номер класса должен быть от 1 до 11!")
                    else:
                        raise AttributeError("Номер класса должен быть цифрой от 1 до 11!")
                else:
                    raise AttributeError("Школьный класс должен содержать цифру от 1 до 11"
                                         " и заглавную букву русского алфавита!")
            elif homeroom_class[i - 1] in alphabet:
                if homeroom_class[0].isdigit():
                    if int(str(homeroom_class[0])) in range(1, 12):
                        self._homeroom_class = homeroom_class
                    else:
                        raise AttributeError("Номер класса должен быть от 1 до 11!")
                else:
                    raise AttributeError("Номер класса должен быть цифрой от 1 до 11!")
            else:
                raise AttributeError("Школьный класс должен содержать цифру от 1 до 11"
                                     " и заглавную букву русского алфавита!")
            teachers[str(self._homeroom_class)] = str(self.name) + ' ' + str(self.last_name)
        self._subjects = subjects

    def set_class(self, new_homeroom_class):
        teachers[new_homeroom_class] = teachers.pop(self._homeroom_class)
        self._homeroom_class = new_homeroom_class
        print(f'{self.name} {self.last_name} теперь является классным руководителем в {self._homeroom_class}')

    def get_class(self):
        print(f'{self.name} {self.last_name} является классным руководителем в {self._homeroom_class}')

    def __repr__(self):
        return (f'Учитель: {self.name} {self.last_name}, предмет: {self._subjects},'
                f' классный руководитель в: {self._homeroom_class}')

    def __str__(self):
        return (f'{self.name} {self.last_name} преподает {self._subjects}. {self.name} {self.last_name}'
                f' является классным руководителем в {self._homeroom_class} классе')
