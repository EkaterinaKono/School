class Human:
    name: str
    last_name: str
    __id: int
    ids = set()

    def __init__(self, name, last_name, id: int = None):
        self.name = name
        self.last_name = last_name
        if id:
            if id in Human.ids:
                raise Exception('Переданный id уже существует!')
            self.__id = id
        else:
            self.__id = max(Human.ids) + 1
        Human.ids.add(self.__id)

    def __hash__(self):
        return hash(self.name + self.last_name)

    def __lt__(self, other):
        return str(self) < str(other)
