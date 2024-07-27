from School.student import Student
from School.teacher import Teacher
from School.CLASS import Class

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

teacher1 = Teacher("Василий", "Андреевич", ["Математика"], "11А")
print(teacher1)
teacher2 = Teacher("Олег", "Сергеевич", ["Физика"], "7Б")
print(teacher2)
print(Teacher.teachers)

v = Teacher.set_dict_teachers()

print(v)
type(v)


class1 = Class(11, "А")
print(class1)

#print(Student.studentss)
#print(Teacher.teachers)
#print(type(Teacher.set_dict_teachers()))


