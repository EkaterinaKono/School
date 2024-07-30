from human import Human
from common import studentss


class Student(Human):
    _class: "Class"

    def __init__(self, name, last_name, group):
        self.name = name
        self.last_name = last_name
        self._class = group
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
