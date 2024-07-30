from School.student import Student
from School.teacher import Teacher
from School.CLASS import Class
from teacher import teachers
from student import studentss

student1 = Student("Игорь", "Петров", "11А")
print(student1)
student2 = Student("Алексей", "Иванов", "11А")
print(student2)
student3 = Student("Василий", "Петров", "11А")
print(student3)
student4 = Student("Мария", "Сидорова", "7Б")
print(student4.__repr__())
student5 = Student("Ирина", "Сергеева", "7Б")
print(student5)
student6 = Student("Анна", "Богданова", "11А")
student7 = Student("Денис", "Григорьев", "11А")

teacher1 = Teacher("Василий", "Андреевич", ["Математика"], "11А")
print(teacher1)
teacher2 = Teacher("Олег", "Сергеевич", ["Физика"], "7Б")
print(teacher2)
print(teachers)
print(studentss)


class1 = Class(11, "А")
print(class1)
print(class1.__repr__())

print(class1)

student2.get_class()
print(studentss)
print()

for i in class1:
    print(i)

student3.get_class()
print()

class1["Петров"]

class1._students.append("Вероника Невзорова")

print(class1)
student1.get_class()

teacher1.get_class()
print()
print(class1)
class1._students.remove("Алексей Иванов")

for i in class1:
    print(i)

print()
print(class1)

print(class1._students)

class1.write_csv("11A.csv")


class1.read_csv("11A.csv")

class2 = Class(7, "Б")
print(class2)

class2._students.append("Иван Иванов")
class2._students.append("Даниил Чижов")
print(class2)

class2.write_csv("7Б.csv")
class2.read_csv("7Б.csv")
