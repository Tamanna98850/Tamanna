# OOP Notes in Python
# 1. OOP kya hai?
# OOP = Object-Oriented Programming
# OOP ek programming approach hai jisme program ko objects aur classes ke form mein organize kiya jata hai.

# Real-life example:
# Agar hume Car ko program mein represent karna hai:
# Car ka name
# Car ka color
# Car ki speed
# ye attributes/properties hain.

# Aur:

# start()
# stop()
# accelerate()

# ye methods/behaviours hain.

# 2. Class kya hoti hai?

# Class ek blueprint/template hoti hai, jiske basis par objects banaye jaate hain.

# Syntax:
# class Student:
#     name = "Rahul"
#     age = 20

# Yahan Student ek class hai.

# 3. Object kya hota hai?

# Object class ka instance hota hai.

# Example:

# class Student:
#     name = "Rahul"
#     age = 20

# s1 = Student()

# print(s1.name)
# print(s1.age)

# Output:

# Rahul
# 20

# Yahan:

# Student → Class
# s1 → Object
# name, age → Attributes
# 4. Constructor __init__()

# __init__() ek special method hai jo object create hone par automatically call hota hai.

# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# s1 = Student("Rahul", 20)

# print(s1.name)
# print(s1.age)

# Output:

# Rahul
# 20
# Important:
# def __init__(self):

# sahi hai.

# ❌ Galat:

# def__init__(self):
# 5. self kya hai?

# self current object ko represent karta hai.

# Example:

# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# Yahan:

# self.name

# current object ka name hai.

# self.age

# current object ka age hai.

# 6. Attributes

# Object ke data ko attributes kaha jata hai.

# Example:
# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# s1 = Student("Aman", 20)
# s2 = Student("Riya", 19)

# print(s1.name)
# print(s2.name)

# Output:

# Aman
# Riya
# 7. Methods

# Class ke andar banaye gaye functions ko methods kehte hain.

# class Student:

#     def __init__(self, name):
#         self.name = name

#     def display(self):
#         print("Student Name:", self.name)

# s1 = Student("Aman")

# s1.display()

# Output:

# Student Name: Aman
# 8. Four Main Pillars of OOP

# OOP ke 4 important pillars hain:

# Encapsulation
# Inheritance
# Polymorphism
# Abstraction
# 9. Encapsulation

# Encapsulation ka matlab data aur methods ko ek single unit/class ke andar bind karna hai.

# Example:

# class BankAccount:

#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def show_balance(self):
#         print(self.balance)

# account = BankAccount(1000)

# account.deposit(500)
# account.show_balance()

# Output:

# 1500
# Simple definition:

# Encapsulation means wrapping data and methods together inside a class.

# 10. Access Modifiers

# Python mein mainly ye conventions use hote hain:

# Public
# self.name

# Directly access kiya ja sakta hai.

# Protected
# self._name

# Single underscore conventionally protected member ko indicate karta hai.

# Private
# self.__name

# Double underscore name ko private-style access deta hai.

# Example:

# class Student:

#     def __init__(self):
#         self.name = "Aman"
#         self._age = 20
#         self.__marks = 90

# s = Student()

# print(s.name)
# print(s._age)
# 11. Inheritance

# Inheritance mein ek class doosri class ke properties aur methods ko use kar sakti hai.

# Example:

# class Animal:

#     def eat(self):
#         print("Animal is eating")


# class Dog(Animal):

#     def bark(self):
#         print("Dog is barking")


# d = Dog()

# d.eat()
# d.bark()

# Output:

# Animal is eating
# Dog is barking

# Yahan:

# Animal → Parent class
# Dog → Child class
# 12. Types of Inheritance

# Python mein common types:

# 1. Single Inheritance
# A
# |
# B
# class A:
#     pass

# class B(A):
#     pass
# 2. Multilevel Inheritance
# A
# |
# B
# |
# C
# 3. Multiple Inheritance
# A   B
#  \ /
#   C
# class A:
#     pass

# class B:
#     pass

# class C(A, B):
#     pass
# 4. Hierarchical Inheritance
#      A
#    /   \
#   B     C

# Ek parent se multiple child classes.

# 5. Hybrid Inheritance

# Do ya zyada inheritance types ka combination.

# 13. Polymorphism

# Polymorphism = One name, multiple forms.

# Example:

# class Dog:

#     def sound(self):
#         print("Bark")


# class Cat:

#     def sound(self):
#         print("Meow")


# d = Dog()
# c = Cat()

# d.sound()
# c.sound()

# Output:

# Bark
# Meow

# Same method name:

# sound()

# lekin behaviour different hai.

# 14. Method Overriding

# Child class parent class ke method ko apne according redefine kare to ise method overriding kehte hain.

# class Animal:

#     def sound(self):
#         print("Animal sound")


# class Dog(Animal):

#     def sound(self):
#         print("Dog barks")


# d = Dog()
# d.sound()

# Output:

# Dog barks
# 15. Abstraction

# Abstraction ka matlab unnecessary implementation details ko hide karke sirf important functionality show karna hai.

# Python mein ABC aur abstractmethod use kiye ja sakte hain.

# from abc import ABC, abstractmethod

# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         pass


# class Dog(Animal):

#     def sound(self):
#         print("Bark")


# d = Dog()
# d.sound()
# 16. Class Variable

# Class variable class ke sabhi objects ke liye common hota hai.

# class Student:

#     school = "ABC School"

#     def __init__(self, name):
#         self.name = name


# s1 = Student("Aman")
# s2 = Student("Riya")

# print(s1.school)
# print(s2.school)
# 17. Instance Variable

# Instance variable har object ka alag data store karta hai.

# class Student:

#     def __init__(self, name):
#         self.name = name

# Yahan:

# self.name

# instance variable hai.

# 18. Class Method

# Class method ko @classmethod decorator ke saath banaya jata hai.

# class Student:

#     school = "ABC School"

#     @classmethod
#     def change_school(cls, name):
#         cls.school = name


# Student.change_school("XYZ School")

# print(Student.school)
# 19. Static Method

# Static method ko @staticmethod decorator ke saath banaya jata hai.

# class Calculator:

#     @staticmethod
#     def add(a, b):
#         return a + b


# print(Calculator.add(10, 20))

# Output:

# 30
# 20. super() Function

# super() parent class ke methods/constructor ko access karne ke liye use hota hai.

# class Animal:

#     def __init__(self, name):
#         self.name = name


# class Dog(Animal):

#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed


# d = Dog("Tommy", "Labrador")

# print(d.name)
# print(d.breed)
# 21. Destructor

# Python mein __del__() object destroy hone ke time call ho sakta hai.

# class Student:

#     def __init__(self):
#         print("Object created")

#     def __del__(self):
#         print("Object destroyed")


# s = Student()
# 22. Complete OOP Example
# class Student:

#     school = "ABC School"

#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Marks:", self.marks)

#     def result(self):
#         if self.marks >= 40:
#             print("Pass")
#         else:
#             print("Fail")


# s1 = Student("Aman", 20, 85)

# s1.display()
# s1.result()

# Output:

# Name: Aman
# Age: 20
# Marks: 85
# Pass
# 23. Important OOP Terms
# Term	Meaning
# Class	Blueprint
# Object	Instance of class
# Attribute	Object/Class data
# Method	Function inside class
# Constructor	__init__()
# self	Current object
# Inheritance	Parent se properties lena
# Encapsulation	Data + methods ko bind karna
# Polymorphism	One name, multiple forms
# Abstraction	Implementation details hide karna
# super()	Parent class access karna
# Destructor	__del__()
# 24. Exam ke liye Short Definitions

# Class:
# Class is a blueprint for creating objects.

# Object:
# Object is an instance of a class.

# Encapsulation:
# Wrapping data and methods together inside a class.

# Inheritance:
# The process by which one class acquires properties and methods of another class.

# Polymorphism:
# The ability of the same interface/method name to have different behaviours.

# Abstraction:
# Hiding unnecessary implementation details and showing essential functionality.

# Constructor:
# __init__() is a special method that is automatically called when an object is initialized

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# p1 = person("Tamanna",17)

# print(p1.name)
# print(p1.age)    

