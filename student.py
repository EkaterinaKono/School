from human import Human
from common import studentss
from common import alphabet


class Student(Human):
    _class: "Class"

    def __init__(self, name: str, last_name: str, group: "Class"):
        i = 0
        self.name = name
        self.last_name = last_name
        for ch in group:
            i += 1
        if i < 2 or i > 3:
            raise AttributeError("Школьный класс должен содержать цифру от 1 до 11 и заглавную букву русского алфавита!")
        elif i == 3:
            if group[i-1] in alphabet:
                if group[0].isdigit() and group[1].isdigit():
                    if int(str(group[0]) + str(group[1])) in range(1, 12):
                        self._class = group
                    else:
                        raise AttributeError("Номер класса должен быть от 1 до 11!")
                else:
                    raise AttributeError("Номер класса должен быть цифрой от 1 до 11!")
            else:
                raise AttributeError("Школьный класс должен содержать цифру от 1 до 11"
                                     " и заглавную букву русского алфавита!")
        elif group[i-1] in alphabet:
            if group[0].isdigit():
                if int(str(group[0])) in range(1, 12):
                    self._class = group
                else:
                    raise AttributeError("Номер класса должен быть от 1 до 11!")
            else:
                raise AttributeError("Номер класса должен быть цифрой от 1 до 11!")
        else:
            raise AttributeError("Школьный класс должен содержать цифру от 1 до 11"
                                 " и заглавную букву русского алфавита!")
        studentss[str(self.name) + ' ' + str(self.last_name)] = str(self._class)

    def set_class(self, new_class):
        self._class = new_class
        print(f'class for student {self.name} {self.last_name} has been changed to ', self._class)
        for i, m in studentss.items():
            if (self.name + " " + self.last_name) == i:
                studentss[i] = self._class

    def get_class(self):
        print(f'{self.name} {self.last_name} is studying in {self._class} class')

    def __repr__(self):
        return f'class: {self._class}, student: {self.name} {self.last_name}'

    def __str__(self):
        return f'{self.name} {self.last_name} is studying in class {self._class}'
