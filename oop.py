
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

########## question ##############
# Python OOP – Class and Object
# Basic Practice Questions with Solutions
# Instructions: Solve each question first, then compare your answer with the solution. Focus on understanding class, object, attributes, and simple methods.
# Question 1 – Create a Class
# Create a class named Student. The class should contain no attributes or methods.
# Solution:
# class Student:
#     pass
# # Question 2 – Create an Object
# # Create a class named Student and create one object named s1.
# # Solution:
# class Student:
#     pass

# s1 = Student()
# # Question 3 – Create Multiple Objects
# # Create a class named Car and create three objects: car1, car2, and car3.
# # Solution:
# class Car:
#     pass

# car1 = Car()
# car2 = Car()
# car3 = Car()
# # Question 4 – Add an Attribute
# # Create a Student class and add a name attribute with the value 'Rahul'. Create an object and display the name.
# # Solution:
# class Student:
#     pass

# s1 = Student()
# s1.name = "Rahul"

# print(s1.name)
# # Question 5 – Create Two Objects with Different Attributes
# # Create a Student class. Create two objects s1 and s2 and give them different names. Display both names.
# # Solution:
# class Student:
#     pass

# s1 = Student()
# s2 = Student()

# s1.name = "Rahul"
# s2.name = "Anushka"

# print(s1.name)
# print(s2.name)
# # Question 6 – Student Details
# # Create a Student class. Create an object and store name, age, and marks as attributes. Display all three.
# # Solution:
# class Student:
#     pass

# s1 = Student()

# s1.name = "Rahul"
# s1.age = 20
# s1.marks = 90

# print(s1.name)
# print(s1.age)
# print(s1.marks)
# # Question 7 – Create a Mobile Class
# # Create a Mobile class and create two objects. Store different brand names for each object and display them.
# # Solution:
# class Mobile:
#     pass

# m1 = Mobile()
# m2 = Mobile()

# m1.brand = "Samsung"
# m2.brand = "Apple"

# print(m1.brand)
# print(m2.brand)
# # Question 8 – Create a Book Class
# # Create a Book class. Create one object and store title and price as attributes. Display the book details.
# # Solution:
# class Book:
#     pass

# b1 = Book()

# b1.title = "Python Programming"
# b1.price = 500

# print("Title:", b1.title)
# print("Price:", b1.price)
# # Question 9 – Add a Method
# # Create a Student class with a method display() that prints 'Welcome to Python OOP'. Create an object and call the method.
# # Solution:
# class Student:

#     def display(self):
#         print("Welcome to Python OOP")

# s1 = Student()
# s1.display()
# # Question 10 – Real-Life Class and Objects
# # Create an Employee class. Create two objects e1 and e2. Store name and salary for each employee and display their details.
# # Solution:
# class Employee:

#     def display(self):
#         print("Name:", self.name)
#         print("Salary:", self.salary)


# e1 = Employee()
# e1.name = "Rahul"
# e1.salary = 30000

# e2 = Employee()
# e2.name = "Anu"
# e2.salary = 35000

# e1.display()
# e2.display()
# # Quick Revision
# # Class = blueprint/template used to create objects.
# # Object = an individual instance created from a class.
# # Attribute = data stored in an object.
# # Method = function defined inside a clas
# ############################
# # Python OOP – Class, Object & Constructor
# # 10 Practice Questions with Solutions
# # Topics covered: Class, Object, Constructor (__init__), self, Instance Variables, Methods, and basic calculations.

# # Question 1 – Student Class
# # Create a Student class with a constructor that accepts the student's name and age. Create one object and display the details.
# # Solution:
# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# s1 = Student("Rahul", 20)

# print("Name:", s1.name)
# print("Age:", s1.age)

# # Question 2 – Employee Class
# # Create an Employee class with a constructor that accepts employee name, employee ID, and salary. Create two objects and display their details.
# # Solution:
# class Employee:

#     def __init__(self, name, emp_id, salary):
#         self.name = name
#         self.emp_id = emp_id
#         self.salary = salary


# e1 = Employee("Rahul", 101, 30000)
# e2 = Employee("Anu", 102, 35000)

# print(e1.name, e1.emp_id, e1.salary)
# print(e2.name, e2.emp_id, e2.salary)

# # Question 3 – Car Class
# # Create a Car class with a constructor that accepts brand, model, and color. Create three different car objects and display their details.
# # Solution:
# class Car:

#     def __init__(self, brand, model, color):
#         self.brand = brand
#         self.model = model
#         self.color = color


# car1 = Car("BMW", "X5", "Black")
# car2 = Car("Audi", "A4", "White")
# car3 = Car("Tesla", "Model 3", "Red")

# print(car1.brand, car1.model, car1.color)
# print(car2.brand, car2.model, car2.color)
# print(car3.brand, car3.model, car3.color)
# # Question 4 – Book Class
# # Create a Book class with a constructor that accepts title, author, and price. Create one object and display all the book details.
# # Solution:
# class Book:

#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price


# b1 = Book("Python Programming", "John", 500)

# print("Title:", b1.title)
# print("Author:", b1.author)
# print("Price:", b1.price)

# # Question 5 – Mobile Class
# # Create a Mobile class with a constructor that accepts brand, model, and storage. Create two objects with different values and display their details.
# # Solution:
# class Mobile:

#     def __init__(self, brand, model, storage):
#         self.brand = brand
#         self.model = model
#         self.storage = storage


# m1 = Mobile("Samsung", "S24", "256GB")
# m2 = Mobile("Apple", "iPhone 16", "128GB")

# print(m1.brand, m1.model, m1.storage)
# print(m2.brand, m2.model, m2.storage)

# # Question 6 – Rectangle Class
# # Create a Rectangle class with a constructor that accepts length and width. Create an object and calculate the area and perimeter.
# # Solution:
# class Rectangle:

#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)


# r1 = Rectangle(10, 5)

# print("Area:", r1.area())
# print("Perimeter:", r1.perimeter())
# # Question 7 – Bank Account
# # Create a BankAccount class with a constructor that accepts account holder name, account number, and balance. Create two objects and display their details.
# # Solution:
# class BankAccount:

#     def __init__(self, holder_name, account_number, balance):
#         self.holder_name = holder_name
#         self.account_number = account_number
#         self.balance = balance


# a1 = BankAccount("Rahul", "12345", 50000)
# a2 = BankAccount("Anu", "67890", 75000)

# print("Account Holder:", a1.holder_name)
# print("Account Number:", a1.account_number)
# print("Balance:", a1.balance)

# print()

# print("Account Holder:", a2.holder_name)
# print("Account Number:", a2.account_number)
# print("Balance:", a2.balance)
# # Question 8 – Student Marks
# # Create a Student class with a constructor that accepts name, roll number, and marks. Create a method display_result() that prints all three details.
# # Solution:
# class Student:

#     def __init__(self, name, roll_number, marks):
#         self.name = name
#         self.roll_number = roll_number
#         self.marks = marks

#     def display_result(self):
#         print("Name:", self.name)
#         print("Roll Number:", self.roll_number)
#         print("Marks:", self.marks)


# s1 = Student("Rahul", 101, 90)

# s1.display_result()
# # Question 9 – Product Class
# # Create a Product class with a constructor that accepts product name, price, and quantity. Create a method calculate_total() that calculates Price × Quantity.
# # Solution:
# class Product:

#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def calculate_total(self):
#         return self.price * self.quantity


# p1 = Product("Laptop", 50000, 2)

# print("Product:", p1.name)
# print("Price:", p1.price)
# print("Quantity:", p1.quantity)
# print("Total:", p1.calculate_total())
# # Question 10 – Movie Class
# # Create a Movie class with a constructor that accepts movie name, director, rating, and year. Create three movie objects and a display() method to show their details.
# # Solution:
# class Movie:

#     def __init__(self, name, director, rating, year):
#         self.name = name
#         self.director = director
#         self.rating = rating
#         self.year = year

#     def display(self):
#         print("Movie:", self.name)
#         print("Director:", self.director)
#         print("Rating:", self.rating)
#         print("Year:", self.year)
#         print()


# movie1 = Movie("3 Idiots", "Rajkumar Hirani", 8.4, 2009)
# movie2 = Movie("Dangal", "Nitesh Tiwari", 8.3, 2016)
# movie3 = Movie("Taare Zameen Par", "Aamir Khan", 8.3, 2007)

# movie1.display()
# movie2.display()
# movie3.display()
# # Quick Revision
# # Class → Blueprint/template for creating objects.
# # Object → Individual instance created from a class.
# # Constructor (__init__) → Special method used to initialize an object.
# # self → Refers to the current object/instance.
# # Method → Function defined inside a class that describes object behavior.

############# OOPs Assignment – Python ##########
# Easy – 5 Questions
# 1.	Create a class Student with attributes name and age. Use a constructor to initialize them and create one object to display the student's details.
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Student Name:", self.name)
#         print("Student Age:", self.age)


# # Create object
# student1 = Student("Tamanna", 17)

# # Display details
# student1.display()

# 2.	Create a class Car with attributes brand and model. Use a constructor and create two objects with different values. Display the details of both cars.
# class Car:

#      def __init__(self, brand, model):
#          self.brand = brand
#          self.model = model
         


# car1 = Car("BMW", "X5")
# car2 = Car("Audi", "A4")


# print(car1.brand, car1.model)
# print(car2.brand, car2.model)

# 3.	Create a class Rectangle with attributes length and width. Use a constructor and create a method area() that returns the area of the rectangle.
# class Rectangle:

#      def __init__(self, length, width):
#          self.length = length
#          self.width = width

#      def area(self):
#          return self.length * self.width

#      def perimeter(self):
#          return 2 * (self.length + self.width)


# r1 = Rectangle(10, 5)

# print("Area:", r1.area())
# print("Perimeter:", r1.perimeter())

# 4.	Create a parent class Animal with a method sound(). Create a child class Dog that inherits from Animal and overrides sound() to print 'Bark'. Create a Dog object and call the method.
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         print("Bark")

# dog1 = Dog()
# dog1.sound()
        
# 5.	Create a class Person with a constructor that accepts name and age. Create two objects and display their information using a method display().
class Person:
    def __init__(self,name,age):
        

           
# Medium – 10 Questions
# 6.	Create a class BankAccount with a constructor that initializes account_holder and balance. Add methods deposit() and withdraw(). Create an object and perform both operations.
# 7.	Create a parent class Employee with attributes name and salary. Create a child class Manager that adds a department attribute. Use constructors in both classes and display all details.
# 8.	Create a parent class Vehicle with a method start(). Create child classes Car and Bike that override start() with different messages. Demonstrate polymorphism using objects of both classes.
# 9.	Create a class Student with a constructor for name and marks. Add a method calculate_grade() that returns A, B, C, D, or F based on the marks. Create at least three objects and display their grades.
# 10.	Create a parent class Shape with a method area(). Create child classes Circle and Rectangle that override area(). Store both objects in a list and call area() for each object using a loop.
# 11.	Create a class Product with a constructor that accepts name, price, and quantity. Add a method total_price() to calculate price × quantity. Create three product objects and display their total prices.
# 12.	Create a parent class Animal with a constructor that accepts name. Create child classes Dog and Cat. Each child class should have its own sound() method. Use a loop to demonstrate polymorphism.
# 13.	Create a class Employee with a constructor that accepts name and salary. Create a child class Developer that adds a programming_language attribute. Create two Developer objects and display all information.
# 14.	Create a parent class Person with a method introduce(). Create child classes Student and Teacher that override introduce() differently. Create objects of both classes and demonstrate polymorphism.
# 15.	Create a class Book with a constructor for title, author, and price. Add a method display(). Create a child class EBook that adds file_size. Use inheritance and constructors to display complete EBook information.
# Hard – 10 Questions
# 16.	Create an Employee Management System using a parent class Employee and child classes Developer, Designer, and Manager. Each child class must override a work() method differently. Create multiple objects and demonstrate polymorphism.
# 17.	Create a payment system with a parent class Payment containing a constructor for amount and an abstract-style pay() method. Create child classes UPI, CreditCard, and NetBanking that implement pay() differently. Demonstrate polymorphism.
# 18.	Create a school management system using a parent class Person and child classes Student and Teacher. Use constructors, inheritance, and overridden display() methods. Store different objects in one list and display their details polymorphically.
# 19.	Create a Shape hierarchy with a parent class Shape and child classes Circle, Rectangle, and Triangle. Each class must implement its own area() method. Store all shapes in a list and calculate their areas using a single loop.
# 20.	Create a banking system with a parent class BankAccount and child classes SavingsAccount and CurrentAccount. Implement deposit() and withdraw() with different rules for each account type. Demonstrate inheritance and polymorphism.
# 21.	Create an online shopping system with a Product parent class and child classes Electronics, Clothing, and Grocery. Use constructors to initialize common and specific attributes. Override a final_price() method for each category and display prices polymorphically.
# 22.	Create a university role system with a parent class UniversityMember and child classes Student, Professor, and Researcher. Each child class should have different behavior for a common method activity(). Use constructors and polymorphism to display each member's activity.
# 23.	Create a transportation system with a parent class Transport and child classes Bus, Train, and Flight. Each child class should override calculate_fare(distance). Use a list of transport objects and calculate fares polymorphically for a given distance.
# 24.	Create a company payroll system with a parent class Employee and child classes FullTimeEmployee, PartTimeEmployee, and Freelancer. Each class should calculate salary differently using a common calculate_salary() method. Use constructors, inheritance, and polymorphism.
# 25.	Create a library management system with a parent class LibraryItem and child classes Book, Magazine, and DVD. Use constructors for common and unique attributes. Override a method borrow_period() in each child class and display the borrowing period for different objects using polymorphism.

# Topics Covered: Class, Object, Constructor (__init__), Instance Methods, Inheritance, 