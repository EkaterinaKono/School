from common import ids


class Human:
    name: str
    last_name: str
    __id: int

    def __init__(self, name: str, last_name: str, id: int = None):
        if isinstance(name, str):
            self.name = name
        else:
            raise AttributeError('Именем может быть только строка')
        if isinstance(last_name, str):
            self.last_name = last_name
        else:
            raise AttributeError('Фамилией может быть только строка')
        if id:
            if id in ids:
                raise AttributeError('Переданный id уже существует!')
            self.__id = id
        else:
            self.__id = max(ids) + 1
        ids.add(self.__id)

    def __hash__(self):
        return hash(self.name + self.last_name)

    def __lt__(self, other):
        return str(self) < str(other)

    def __repr__(self):
        return f'name: {self.name}, lastname: {self.last_name}'

    def __str__(self):
        return f'{self.name} {self.last_name}'
