import unittest
from human import Human
from student import Student
from teacher import Teacher


TRUE_NAMES = ["Илья", "Мария", "Олег"]
TRUE_LAST_NAMES = ["Петров", "Иванова", "Сидоров"]

WRONG_NAMES = [123, 7.6]
WRONG_LAST_NAMES = [4756, 856795]

TRUE_IDS = [1, 2, 3, 4, 5]
WRONG_IDS = [1, 2, 3, 4, 5]

TEST_HUMAN1 = Human("Андрей", "Авдеев", 20)
TEST_HUMAN2 = Human("Яков", "Яшин", 21)
TEST_HUMAN3 = Human("Анна", "Агеева", 22)
TEST_HUMAN4 = Human("Яна", "Яковлева", 23)

TEST_HUMANS = [TEST_HUMAN1, TEST_HUMAN2, TEST_HUMAN3, TEST_HUMAN4]

CORRECT_CLASSES = ["11А", "1Б", "8В", "3Г"]
INCORRECT_CLASSES = ["123", "ВА", "1D", "12А"]


class SchoolTests(unittest.TestCase):

    def test_human_name_lastname(self):
        n = 6
        for name in TRUE_NAMES:
            for last_name in TRUE_LAST_NAMES:
                test_human = Human(name, last_name, n)
                n += 1
        for name in WRONG_NAMES:
            for last_name in WRONG_LAST_NAMES:
                try:
                    test_human = Human(name, last_name, n)
                    n += 1
                except AttributeError:
                    pass
                else:
                    raise AssertionError("Создали человека с неверным именем")

    def test_human_id(self):
        for i in TRUE_IDS:
            test_human = Human("Иван", "Иванов", i)
        for i in WRONG_IDS:
            try:
                test_human = Human("Петр", "Петров", i)
            except AttributeError:
                pass
            else:
                AssertionError("Создали человека с уже существующим id")

    def test_human_lt(self):
        self.assertEqual(TEST_HUMAN1 < TEST_HUMAN2, 0 < 1)
        self.assertEqual(TEST_HUMAN2 < TEST_HUMAN1, 1 < 0)
        self.assertEqual(TEST_HUMAN4 > TEST_HUMAN3, 1 > 0)
        self.assertEqual(TEST_HUMAN4 < TEST_HUMAN3, 1 < 0)

    def test_human_hash(self):
        for human in TEST_HUMANS:
            self.assertEqual(hash(human), hash(human.name+human.last_name))

    def test_human_str(self):
        for human in TEST_HUMANS:
            self.assertEqual(human.__str__(), human.name + " " + human.last_name)

    def test_student_class(self):
        for i in CORRECT_CLASSES:
            test_student = Student("Иван", "Иванов", i)
        for i in INCORRECT_CLASSES:
            try:
                test_student = Student("Иван", "Иванов", i)
            except AttributeError:
                pass
            else:
                AssertionError("Создали школьника с неверно заданным классом")

    def test_teacher_class(self):
        for i in CORRECT_CLASSES:
            test_teacher = Teacher("Иван", "Иванович", ["История"], i)
        for i in INCORRECT_CLASSES:
            try:
                test_teacher = Teacher("Иван", "Иванович", ["История"], i)
            except AttributeError:
                pass
            else:
                AssertionError("Создали учителя с неверно заданным классом")
