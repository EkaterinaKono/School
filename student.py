from human import Human


class Student(Human):
    _class: "Class"
    studentss = {}

    def __init__(self, name, last_name, group):
        self.name = name
        self.last_name = last_name
        self._class = group
        Student.studentss[str(self.name) + ' ' + str(self.last_name)] = str(self._class)

    def set_class(self, new_class):
        self._class = new_class
        print('class has been changed to ', self._class)

    def get_class(self):
        return f'{self.name} {self.last_name} is studying in {self._class} class'

    def __repr__(self):
        return f'class: {self._class}, student: {self.name} {self.last_name}'

    def __str__(self):
        return f'{self.name} {self.last_name} is studying in class {self._class}'
