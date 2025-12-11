"""ДЗ 14.1. Виняток користувача
Модифікуйте клас Група (завдання минулої лекції) так, щоб при спробі
додавання до групи більше 10-ти студентів, було порушено виняток користувача.
Таким чином потрібно створити ще й виняток користувача для цієї ситуації.
І обробити його поза межами класу. Тобто. потрібно перехопити цей виняток,
при спробі додавання 11-го студента
"""


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.gender} {self.age} {self.first_name} {self.last_name}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()} {self.record_book}"


class GroupExeption(Exception):  # роблю виняток
    pass


class Group:
    max_students = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.max_students:  # перевіряю чи не більше 10 студентів
            raise GroupExeption
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student

    def __str__(self):
        all_students = ", ".join(str(s) for s in self.group)
        return f"Number:{self.number} : {all_students} "


st1 = Student("Male", 30, "Steve", "Jobs", "AN142")
st2 = Student("Female", 25, "Liza", "Taylor", "AN145")
st3 = Student("Male", 25, "Annik", "Jobs", "AN145")
st4 = Student("Female", 25, "Vera", "Taylor", "AN145")
st5 = Student("Male", 25, "Stev", "Jobs", "AN145")
st6 = Student("Female", 25, "Lizaveta", "Taylor", "AN145")
st7 = Student("Male", 25, "Tom", "Jobs", "AN145")
st8 = Student("Female", 25, "Kris", "Taylor", "AN145")
st8 = Student("Male", 25, "Stevenson", "Jobs", "AN145")
st9 = Student("Female", 25, "Luiza", "Taylor", "AN145")
st10 = Student("Male", 25, "Tonny", "Jobs", "AN145")
st11 = Student("Female", 25, "Angelika", "Taylor", "AN145")
gr = Group("PD1")
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
gr.add_student(st11)
print(gr)
assert str(gr.find_student("Jobs")) == str(st1), "Test1"
assert gr.find_student("Jobs2") is None, "Test2"
assert (
    isinstance(gr.find_student("Jobs"), Student) is True
), "Метод поиска должен возвращать экземпляр"

gr.delete_student("Taylor")
print(gr)  # Only one student

gr.delete_student("Taylor")  # No error!
