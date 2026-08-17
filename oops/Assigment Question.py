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
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Person Name:", self.name)
#         print("Person Age:", self.age)

# person1 = Person("Tamanna",17)
# person2 = Person("Tamanna B",17)

# person1.display()  
# person2.display()       
        
# Medium – 10 Questions
# 6.	Create a class BankAccount with a constructor that initializes account_holder and balance. Add methods deposit() and withdraw(). Create an object and perform both operations.
# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposited:", amount)
#         print("Current Balance:", self.balance)

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Withdrawn:", amount)
#             print("Current Balance:", self.balance)
#         else:
#             print("Insufficient Balance")


# # Create object
# account = BankAccount("Tamanna", 5000)

# # Perform operations
# account.deposit(2000)
# account.withdraw(1500)
# 7.	Create a parent class Employee with attributes name and salary. Create a child class Manager that adds a department attribute. Use constructors in both classes and display all details.
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary


# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department

#     def display(self):
#         print("Name:", self.name)
#         print("Salary:", self.salary)
#         print("Department:", self.department)


# manager = Manager("Tamanna", 50000, "IT")
# manager.display()

# 8.	Create a parent class Vehicle with a method start(). Create child classes Car and Bike that override start() with different messages. Demonstrate polymorphism using objects of both classes.
# class Vehicle:
#     def start(self):
#         print("Vehicle is starting")


# class Car(Vehicle):
#     def start(self):
#         print("Car starts with a key")


# class Bike(Vehicle):
#     def start(self):
#         print("Bike starts with a button")


# vehicles = [Car(), Bike()]

# for vehicle in vehicles:
#     vehicle.start()

# 9.	Create a class Student with a constructor for name and marks. Add a method calculate_grade() that returns A, B, C, D, or F based on the marks. Create at least three objects and display their grades.
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def calculate_grade(self):
#         if self.marks >= 90:
#             return "A"
#         elif self.marks >= 75:
#             return "B"
#         elif self.marks >= 60:
#             return "C"
#         elif self.marks >= 40:
#             return "D"
#         else:
#             return "F"


# students = [
#     Student("Rahul", 92),
#     Student("Priya", 78),
#     Student("Aman", 55)
# ]

# for student in students:
#     print(student.name, "Grade:", student.calculate_grade())

# 10.	Create a parent class Shape with a method area(). Create child classes Circle and Rectangle that override area(). Store both objects in a list and call area() for each object using a loop.
# import math

# class Shape:
#     def area(self):
#         pass


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2


# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width


# shapes = [
#     Circle(5),
#     Rectangle(10, 4)
# ]

# for shape in shapes:
#     print("Area:", shape.area())

# 11.	Create a class Product with a constructor that accepts name, price, and quantity. Add a method total_price() to calculate price × quantity. Create three product objects and display their total prices.
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def total_price(self):
#         return self.price * self.quantity


# products = [
#     Product("Laptop", 50000, 1),
#     Product("Mouse", 500, 2),
#     Product("Keyboard", 1000, 1)
# ]

# for product in products:
#     print(product.name, "Total Price:", product.total_price())

# 12.	Create a parent class Animal with a constructor that accepts name. Create child classes Dog and Cat. Each child class should have its own sound() method. Use a loop to demonstrate polymorphism.
# class Animal:
#     def __init__(self, name):
#         self.name = name


# class Dog(Animal):
#     def sound(self):
#         print(self.name, "says Woof")


# class Cat(Animal):
#     def sound(self):
#         print(self.name, "says Meow")


# animals = [
#     Dog("Tommy"),
#     Cat("Kitty")
# ]

# for animal in animals:
#     animal.sound()

# 13.	Create a class Employee with a constructor that accepts name and salary. Create a child class Developer that adds a programming_language attribute. Create two Developer objects and display all information.
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary


# class Developer(Employee):
#     def __init__(self, name, salary, programming_language):
#         super().__init__(name, salary)
#         self.programming_language = programming_language

#     def display(self):
#         print("Name:", self.name)
#         print("Salary:", self.salary)
#         print("Language:", self.programming_language)


# developer1 = Developer("Tamanna", 60000, "Python")
# developer2 = Developer("Rahul", 70000, "JavaScript")

# developer1.display()
# print()
# developer2.display()

# 14.	Create a parent class Person with a method introduce(). Create child classes Student and Teacher that override introduce() differently. Create objects of both classes and demonstrate polymorphism.
# class Person:
#     def introduce(self):
#         print("I am a person")


# class Student(Person):
#     def introduce(self):
#         print("I am a student")


# class Teacher(Person):
#     def introduce(self):
#         print("I am a teacher")


# people = [
#     Student(),
#     Teacher()
# ]

# for person in people:
#     person.introduce()

# 15.	Create a class Book with a constructor for title, author, and price. Add a method display(). Create a child class EBook that adds file_size. Use inheritance and constructors to display complete EBook information.
# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price

#     def display(self):
#         print("Title:", self.title)
#         print("Author:", self.author)
#         print("Price:", self.price)


# class EBook(Book):
#     def __init__(self, title, author, price, file_size):
#         super().__init__(title, author, price)
#         self.file_size = file_size

#     def display(self):
#         super().display()
#         print("File Size:", self.file_size, "MB")


# ebook = EBook("Python Programming", "John", 500, 10)
# ebook.display()

# Hard – 10 Questions

# 16.	Create an Employee Management System using a parent class Employee and child classes Developer, Designer, and Manager. Each child class must override a work() method differently. Create multiple objects and demonstrate polymorphism.
# class Employee:
#     def __init__(self, name):
#         self.name = name

#     def work(self):
#         print(self.name, "is working")


# class Developer(Employee):
#     def work(self):
#         print(self.name, "is writing code")


# class Designer(Employee):
#     def work(self):
#         print(self.name, "is designing UI")


# class Manager(Employee):
#     def work(self):
#         print(self.name, "is managing the team")


# employees = [
#     Developer("Rahul"),
#     Designer("Priya"),
#     Manager("Aman")
# ]

# for employee in employees:
#     employee.work()

# 17.	Create a payment system with a parent class Payment containing a constructor for amount and an abstract-style pay() method. Create child classes UPI, CreditCard, and NetBanking that implement pay() differently. Demonstrate polymorphism.
# class Payment:
#     def __init__(self, amount):
#         self.amount = amount

#     def pay(self):
#         pass


# class UPI(Payment):
#     def pay(self):
#         print("Paid", self.amount, "using UPI")


# class CreditCard(Payment):
#     def pay(self):
#         print("Paid", self.amount, "using Credit Card")


# class NetBanking(Payment):
#     def pay(self):
#         print("Paid", self.amount, "using Net Banking")


# payments = [
#     UPI(1000),
#     CreditCard(2000),
#     NetBanking(3000)
# ]

# for payment in payments:
#     payment.pay()

# 18.	Create a school management system using a parent class Person and child classes Student and Teacher. Use constructors, inheritance, and overridden display() methods. Store different objects in one list and display their details polymorphically.
# class Person:
#     def __init__(self, name):
#         self.name = name

#     def display(self):
#         print("Name:", self.name)


# class Student(Person):
#     def __init__(self, name, grade):
#         super().__init__(name)
#         self.grade = grade

#     def display(self):
#         print("Student:", self.name)
#         print("Grade:", self.grade)


# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject

#     def display(self):
#         print("Teacher:", self.name)
#         print("Subject:", self.subject)


# people = [
#     Student("Rahul", "10th"),
#     Teacher("Priya", "Python")
# ]

# # for person in people:
# #     person.display()
# #     print()

# # 19.	Create a Shape hierarchy with a parent class Shape and child classes Circle, Rectangle, and Triangle. Each class must implement its own area() method. Store all shapes in a list and calculate their areas using a single loop.
# import math

# class Shape:
#     def area(self):
#         pass


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2


# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width


# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height


# shapes = [
#     Circle(5),
#     Rectangle(10, 4),
#     Triangle(8, 6)
# ]

# for shape in shapes:
#     print("Area:", shape.area())

# 20.	Create a banking system with a parent class BankAccount and child classes SavingsAccount and CurrentAccount. Implement deposit() and withdraw() with different rules for each account type. Demonstrate inheritance and polymorphism.
# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposited:", amount)

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Withdrawn:", amount)
#         else:
#             print("Insufficient balance")


# class SavingsAccount(BankAccount):
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Savings withdrawal:", amount)
#         else:
#             print("Insufficient balance")


# class CurrentAccount(BankAccount):
#     def withdraw(self, amount):
#         if amount <= self.balance + 10000:
#             self.balance -= amount
#             print("Current account withdrawal:", amount)
#         else:
#             print("Withdrawal limit exceeded")


# accounts = [
#     SavingsAccount("Rahul", 5000),
#     CurrentAccount("Priya", 5000)
# ]

# for account in accounts:
#     account.deposit(1000)
#     account.withdraw(3000)
#     print("Balance:", account.balance)
#     print()

# # 21.	Create an online shopping system with a Product parent class and child classes Electronics, Clothing, and Grocery. Use constructors to initialize common and specific attributes. Override a final_price() method for each category and display prices polymorphically.
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def final_price(self):
#         return self.price


# class Electronics(Product):
#     def final_price(self):
#         return self.price * 0.90


# class Clothing(Product):
#     def final_price(self):
#         return self.price * 0.80


# class Grocery(Product):
#     def final_price(self):
#         return self.price * 0.95


# products = [
#     Electronics("Laptop", 50000),
#     Clothing("Shirt", 2000),
#     Grocery("Rice", 1000)
# ]

# for product in products:
#     print(product.name, "Final Price:", product.final_price())

# # 22.	Create a university role system with a parent class UniversityMember and child classes Student, Professor, and Researcher. Each child class should have different behavior for a common method activity(). Use constructors and polymorphism to display each member's activity.
# class UniversityMember:
#     def __init__(self, name):
#         self.name = name

#     def activity(self):
#         pass


# class Student(UniversityMember):
#     def activity(self):
#         print(self.name, "is attending classes")


# class Professor(UniversityMember):
#     def activity(self):
#         print(self.name, "is teaching students")


# class Researcher(UniversityMember):
#     def activity(self):
#         print(self.name, "is doing research")


# members = [
#     Student("Rahul"),
#     Professor("Priya"),
#     Researcher("Aman")
# ]

# for member in members:
#     member.activity()

# # 23.	Create a transportation system with a parent class Transport and child classes Bus, Train, and Flight. Each child class should override calculate_fare(distance). Use a list of transport objects and calculate fares polymorphically for a given distance.
# class Transport:
#     def calculate_fare(self, distance):
#         pass


# class Bus(Transport):
#     def calculate_fare(self, distance):
#         return distance * 2


# class Train(Transport):
#     def calculate_fare(self, distance):
#         return distance * 3


# class Flight(Transport):
#     def calculate_fare(self, distance):
#         return distance * 8


# transports = [
#     Bus(),
#     Train(),
#     Flight()
# ]

# distance = 100

# for transport in transports:
#     print("Fare:", transport.calculate_fare(distance))

# # 24.	Create a company payroll system with a parent class Employee and child classes FullTimeEmployee, PartTimeEmployee, and Freelancer. Each class should calculate salary differently using a common calculate_salary() method. Use constructors, inheritance, and polymorphism.
# class Employee:
#     def __init__(self, name):
#         self.name = name

#     def calculate_salary(self):
#         pass


# class FullTimeEmployee(Employee):
#     def __init__(self, name, monthly_salary):
#         super().__init__(name)
#         self.monthly_salary = monthly_salary

#     def calculate_salary(self):
#         return self.monthly_salary


# class PartTimeEmployee(Employee):
#     def __init__(self, name, hours, rate):
#         super().__init__(name)
#         self.hours = hours
#         self.rate = rate

#     def calculate_salary(self):
#         return self.hours * self.rate


# class Freelancer(Employee):
#     def __init__(self, name, projects, rate):
#         super().__init__(name)
#         self.projects = projects
#         self.rate = rate

#     def calculate_salary(self):
#         return self.projects * self.rate


# employees = [
#     FullTimeEmployee("Rahul", 50000),
#     PartTimeEmployee("Priya", 80, 300),
#     Freelancer("Aman", 5, 5000)
# ]

# for employee in employees:
#     print(employee.name, "Salary:", employee.calculate_salary())

# # 25.	Create a library management system with a parent class LibraryItem and child classes Book, Magazine, and DVD. Use constructors for common and unique attributes. Override a method borrow_period() in each child class and display the borrowing period for different objects using polymorphism.
# class LibraryItem:
#     def __init__(self, title):
#         self.title = title

#     def borrow_period(self):
#         pass


# class Book(LibraryItem):
#     def borrow_period(self):
#         return 14


# class Magazine(LibraryItem):
#     def borrow_period(self):
#         return 7


# class DVD(LibraryItem):
#     def borrow_period(self):
#         return 3


# items = [
#     Book("Python Programming"),
#     Magazine("Technology Today"),
#     DVD("Learning Python")
# ]

# for item in items:
#     print(item.title, "->", item.borrow_period(), "days")

# Topics Covered: Class, Object, Constructor (__init__), Instance Methods, Inheritance, 