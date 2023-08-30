# class ім'я(класс для наследования)
# тілшо класу

class Student:
    spec = "CS"
    def __init__(self, name, age):
        self.__name = name # __name - приватне поле, name - публічне
        self.__age = age

    def get_info(self):
        return self.create_row_info()

    def __create_row_info(self):
        return f"Name: {self.__name}, Age: {self.__age}"

    #setter, getter
    def set_name(self, name: str):
        if name.isalpha() and len(name)>=2:
            self.__name =name
        else:
            print("Wrong")

    def get_name(self):
        return self.__name

    def set_age(self, age: int):
        if 1<= self.__age < 200:
            self.__age = age
        else:
            print('Wrong')

    def get_age(self):
        return self.__age


# s1 = Student("Valeriy", 28)
# print(s1.name)
#
# s2 = Student("Turbay", 26)
# print(s2.name)

# count = int(input("Number of users: "))
# users = [Student("Alex", 20),
#          Student("Den", 21)]
# for i in range(count):
#     name = input(f"Enter name of user #{i}:")
#     age = input(f"Enter age of user #{i}:")
#     users.append(Student(name, age))
#
# for user in users:
#     print(user.get_info())


# s1 = Student("Alex", 20)
#
# print(s1.get_name())
# s1.set_name("John")
# print(s1.get_name())


class City:
    def __init__(self, name, region, country, population, postal_code, phone_code):
        self.__name = name
        self.__region = region
        self.__country = country
        self.__population = population
        self.__postal_code = postal_code
        self.__phone_code = phone_code

    def input_data(self):
        self.__name = input("Enter city name: ")
        self.__region = input("Enter region name: ")
        self.__country = input("Enter country name: ")
        self.__population = int(input("Enter population: "))
        self.__postal_code = input("Enter postal code: ")
        self.__phone_code = input("Enter phone code: ")

    def display_data(self):
        print("City:", self.__name)
        print("Region:", self.__region)
        print("Country:", self.__country)
        print("Population:", self.__population)
        print("Postal Code:", self.__postal_code)
        print("Phone Code:", self.__phone_code)

    def get_name(self):
        return self.__name

    def get_region(self):
        return self.__region

    def get_country(self):
        return self.__country

    def get_population(self):
        return self.__population

    def get_postal_code(self):
        return self.__postal_code

    def get_phone_code(self):
        return self.__phone_code

# Создайте класс «Дробь». Необходимо хранить в полях класса:
# числитель и знаменатель. Реализуйте методы класса для ввода данных,
# вывода данных, реализуйте доступ к отдельным полям через методы класса.
# Также создайте методы класса для выполнения арифметических операций
# (сложение, вычитание, умножение, деление, и т.д.).

class Division:
    def __init__(self, num, denum):
        self.__num = num
        self.__denum = denum

    def get_division(self):
        print(f'{self.__num}/{self.__denum}')

    def get_num(self):
        return self.__num

    def get_denum(self):
        return self.__denum

    def add_parts(self, num, denum):
        result_num = self.__num * denum + num * self.__denum
        result_denum = self.__denum * denum
        print(f"{result_num}/{result_denum}")

    def subtract_parts(self, num, denum):
        result_num = self.__num * denum - num * self.__denum
        result_denum = self.__denum * denum
        print(f"{result_num}/{result_denum}")

    def multiply_parts(self, num, denum):
        result_num = self.__num * num
        result_denum = self.__denum * denum
        print(f"{result_num}/{result_denum}")

    def divide_parts(self, num, denominator):
        result_num = self.__num * denominator
        result_denum = self.__denum * num
        print(f"{result_num}/{result_denum}")

# d1 = Division(1, 2)
# d1.get_division()
# d1.add_parts(1,2)
# d1.subtract_parts(1,4)
# d1.multiply_parts(4,4)
# d1.divide_parts(1,2)

# Статичные методы staticmethod
class MyClass:

    var = 0

    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def hello():
        print("Hello")

    @classmethod
    def cl_method(cls):
        cls.var += 1
        print("var = ", cls.var)

    def x(self):
        print("asd")

# m = Math()
# x = m.sum(5, 6)
# Math.hello()
# print(x)

# Успадкування та інкапсуляція + поліморфізм
# Похідний класс(дочірній)
# Базовий (батьковський)

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self._gender = gender #_ - protected

    def get_info(self):
        return f"Person: {self.name}, {self.age}, {self._gender}"

    def get_hi(self, mess):
        return f"{mess}! I am {self.name}"

class Student(Person):
    spec = "CS"
    def __init__(self, name, age, gender, islive):
        super().__init__(name, age, gender)
        self.islive = islive

    @staticmethod
    def is_succesfull(score):
        return score > 6

    def get_info(self):
        return f"Student: {self.name}, {self.age}, {self.spec}, {self._gender}, {self.islive}"

class Employee(Person):

    def __init__(self, name, age, gender, salary):
        super().__init__(name, age, gender)
        self.salary = salary

    def get_info(self):
        return f"Person: {self.name}, {self.age}, {self._gender}. {self.salary}"

# p1 = Person("Den", 50)
# print(p1.get_info())
# print(p1.get_hi("Hello"))

# s1 = Student("Den", 23, "Male", True)
# p1 = Person("Alex", "Male", 50)
# print(s1.get_info())
# print(p1.get_info())
# print(s1.is_succesfull(10))


# MRO - MASS HERITAGE
# Дочірній клас успадковує декілька батьківських классів

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def show_book_info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}")

class File:
    def __init__(self, size, src):
        self.size = size
        self.src = src
    def show_file_info(self):
        print(f"Size: {self.size}\nDef: {self.src}")

class EBook(Book, File):
    def __init__(self, title, author, size, src):
        Book.__init__(self, title, author)
        File.__init__(self, size, src)


# eb1 = EBook("Book", "Den", 100, '/sss/sss')
#
# eb1.show_file_info()
# eb1.show_book_info()
#
# print(EBook.mro())


# class C1:
#     def hi(self):
#         print("Hi from c1")
#
# class C2(C1):
#     def hi(self):
#         print("Hi from c2")
#
# class C3(C1):
#     def hi(self):
#         print("Hi from c3")
#
# class C4(C2, C3):
#     pass
#
# obj = C4()
# obj.hi()
# print(C4.mro())

import math
class Point:

    def __new__(cls, *args, **kwargs):
        print(f"magic new {cls}")
        return super().__new__(cls)
    def __init__(self, x, y):
        print("magic init")
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

n1 = Point(5, 6)
n2 = Point(10, 5)

print(n1)

# print(math.sqrt(((n1.x-n2.x) ** 2) + ((n1.y-n2.y) ** 2)))

# double underscore (dunder methods)