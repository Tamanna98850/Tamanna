###################### Python OOP Practice Questions ################

# Topics Covered: Polymorphism, Getter & Setter, Encapsulation, Abstraction, @classmethod and @staticmethod
# 1. Polymorphism — 5 Questions
# Q1. Method Overriding
# Question: Create an Animal class with a sound() method. Create Dog and Cat classes that override the sound() method.
# Solution:
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

# Q2. Polymorphism with Different Classes
# Question: Create Car and Bike classes. Both should have a start() method. Write a function that can call start() for both objects.
# Solution:
class Car:
    def start(self):
        print("Car starts with a key")

class Bike:
    def start(self):
        print("Bike starts with a button")

def start_vehicle(vehicle):
    vehicle.start()

car = Car()
bike = Bike()

start_vehicle(car)
start_vehicle(bike)

# Q3. Polymorphism with Same Method Name
# Question: Create Rectangle and Circle classes. Both should have an area() method.
# Solution:
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

r = Rectangle(10, 5)
c = Circle(7)

print(r.area())
print(c.area())

# Q4. Polymorphism with Inheritance
# Question: Create a parent Employee class with a calculate_salary() method. Create FullTimeEmployee and PartTimeEmployee classes that calculate salary differently.
# Solution:
class Employee:
    def calculate_salary(self):
        print("Calculating salary")

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("Salary = ₹50,000")

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        print("Salary = ₹20,000")

employees = [FullTimeEmployee(), PartTimeEmployee()]

for employee in employees:
    employee.calculate_salary()

# Q5. Practical Polymorphism
# Question: Create PDF, Word, and Excel classes. Each should have an open_file() method with different behavior.
# Solution:
class PDF:
    def open_file(self):
        print("Opening PDF file")

class Word:
    def open_file(self):
        print("Opening Word document")

class Excel:
    def open_file(self):
        print("Opening Excel spreadsheet")

files = [PDF(), Word(), Excel()]

for file in files:
    file.open_file()

# 2. Getter & Setter — 5 Questions

# Q6. Getter and Setter for Student Marks
# Question: Create a Student class with a private __marks variable. Use a getter and setter to access and modify marks.
# Solution:
class Student:
    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")

student = Student(80)
print(student.get_marks())
student.set_marks(90)
print(student.get_marks())

# Q7. Getter and Setter for Age
# Question: Create a Person class. Age should not be negative.
# Solution:
class Person:
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative")

person = Person(23)
print(person.get_age())
person.set_age(25)
print(person.get_age())

# Q8. Using @property
# Question: Create a BankAccount class where balance can be accessed using a getter and modified using a setter.
# Solution:
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")

account = BankAccount(5000)
print(account.balance)
account.balance = 8000
print(account.balance)

# Q9. Validate Salary
# Question: Create an Employee class where salary cannot be less than ₹10,000.
# Solution:
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary >= 10000:
            self.__salary = salary
        else:
            print("Salary must be at least ₹10,000")

employee = Employee(25000)
print(employee.salary)
employee.salary = 30000
print(employee.salary)

# Q10. Getter/Setter for Password
# Question: Create a User class where the password is private. The setter should ensure the password has at least 8 characters.
# Solution:
class User:
    def __init__(self, password):
        self.__password = password

    @property
    def password(self):
        return "Password is hidden"

    @password.setter
    def password(self, password):
        if len(password) >= 8:
            self.__password = password
            print("Password updated")
        else:
            print("Password must contain at least 8 characters")

user = User("abc12345")
print(user.password)
user.password = "python123" 

# 3. Encapsulation — 5 Questions

# Q11. Private Variable
# Question: Create a BankAccount class with a private balance. Create methods for deposit and withdrawal.
# Solution:
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.__balance)

account = BankAccount(5000)
account.deposit(2000)
account.withdraw(1000)
account.show_balance()

# Q12. Encapsulation in Student
# Question: Create a Student class where marks are private. Create a method to display whether the student passed or failed.
# Solution:
class Student:
    def __init__(self, marks):
        self.__marks = marks

    def result(self):
        if self.__marks >= 40:
            print("Pass")
        else:
            print("Fail")

student = Student(75)
student.result()

# Q13. Private Password
# Question: Create a User class with a private password. Create a method login() to check whether the entered password is correct.
# Solution:
class User:
    def __init__(self, password):
        self.__password = password

    def login(self, password):
        if password == self.__password:
            print("Login successful")
        else:
            print("Invalid password")

user = User("python123")
user.login("python123")

# Q14. Encapsulation with Validation
# Question: Create a Product class where price is private. Allow price changes only if the new price is greater than 0.
# Solution:
class Product:
    def __init__(self, price):
        self.__price = price

    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Invalid price")

    def get_price(self):
        return self.__price

product = Product(500)
product.set_price(700)
print(product.get_price())

# Q15. Practical Encapsulation
# Question: Create a Mobile class with private battery percentage. Create methods to charge and use the battery.
# Solution:
class Mobile:
    def __init__(self, battery):
        self.__battery = battery

    def charge(self, amount):
        self.__battery += amount
        if self.__battery > 100:
            self.__battery = 100

    def use(self, amount):
        if amount <= self.__battery:
            self.__battery -= amount
        else:
            print("Battery is low")

    def show_battery(self):
        print("Battery:", self.__battery, "%")

mobile = Mobile(50)
mobile.charge(30)
mobile.use(20)
mobile.show_battery()

# 4. Abstraction — 5 Questions

# Q16. Abstract Animal Class
# Question: Create an abstract Animal class with an abstract sound() method. Implement it in Dog.
# Solution:
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog barks")

dog = Dog()
dog.sound()

# Q17. Abstract Shape
# Question: Create an abstract Shape class with an area() method. Implement it for Rectangle.
# Solution:
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle = Rectangle(10, 5)
print(rectangle.area())

# Q18. Abstract Payment System
# Question: Create an abstract Payment class with a pay() method. Implement it using CreditCard and UPI.
# Solution:
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print("Paid ₹", amount, "using Credit Card")

class UPI(Payment):
    def pay(self, amount):
        print("Paid ₹", amount, "using UPI")

p1 = CreditCard()
p2 = UPI()

p1.pay(1000)
p2.pay(500)

# Q19. Abstract Employee
# Question: Create an abstract Employee class with a calculate_salary() method. Create Developer and Manager.
# Solution:
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Developer(Employee):
    def calculate_salary(self):
        print("Developer salary = ₹60,000")

class Manager(Employee):
    def calculate_salary(self):
        print("Manager salary = ₹80,000")

d = Developer()
m = Manager()

d.calculate_salary()
m.calculate_salary()

# Q20. Abstract Vehicle
# Question: Create an abstract Vehicle class with start() and stop() methods. Implement them in Car.
# Solution:
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

car = Car()
car.start()
car.stop()

# 5. @classmethod and @staticmethod — 5 Questions

# Q21. Basic @classmethod
# Question: Create a Student class with a class variable school. Use a class method to change the school name.
# Solution:
class Student:
    school = "ABC School"

    @classmethod
    def change_school(cls, name):
        cls.school = name

print(Student.school)
Student.change_school("XYZ School")
print(Student.school)

# Q22. Class Method as Alternative Constructor
# Question: Create a Student class and use a class method to create a student from a string.
# Solution:
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))

student = Student.from_string("Anushka,23")

print(student.name)
print(student.age)

# Q23. Basic @staticmethod
# Question: Create a Calculator class with a static method to add two numbers.
# Solution:
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(10, 20))

# Q24. Static Method for Validation
# Question: Create a User class with a static method that checks whether an email contains @.
# Solution:
class User:
    @staticmethod
    def valid_email(email):
        return "@" in email

print(User.valid_email("abc@gmail.com"))
print(User.valid_email("abcgmail.com"))

# Q25. Class Method + Static Method Together
# Question: Create a Bank class with a class variable bank_name, a class method to change the bank name, and a static method to validate an account number.
# Solution:
class Bank:
    bank_name = "SBI"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    @staticmethod
    def validate_account(account_number):
        return len(str(account_number)) == 10

print(Bank.bank_name)
Bank.change_bank_name("HDFC")
print(Bank.bank_name)
print(Bank.validate_account(1234567890))


                

