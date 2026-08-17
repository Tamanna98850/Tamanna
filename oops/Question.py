# Question: 1
# Create a Student class with attributes name and age.
#  Constructor se initialize karke ek object banakar student ki details display karni hain.
#Answer 
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)


# s1 = Student("Anu", 20)
# s1.display()

# Question: 2
# Car class banao jisme brand aur model attributes hon.
#  Constructor use karke 2 objects create karo aur dono cars ki details display karo.
#Answer
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


car1 = Car("Toyota", "Fortuner")
car2 = Car("Honda", "City")

car1.display()
car2.display()

#Question 3
# Rectangle class banao jisme length aur width attributes hon aur area() 
# method rectangle ka area return kare.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def area(self):
        return self.length * self.width

r1 = Rectangle(10, 5)

print("Area:", r1.area())

#Question: 4
#  Parent class Animal mein sound() method banao. 
# Child class Dog Animal se inherit kare aur sound() ko override karke "Bark" print kare.

class Animal:
    def sound(self):
        print("Animal makes a sound")




class Dog(Animal):
    def sound(self):
        print("Bark")




dog = Dog()
dog.sound()

#Question: 5 
# Person class banao jisme constructor name aur age accept kare.
#  Do objects create karke display() method se information show karo.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)




p1 = Person("Rahul", 22)
p2 = Person("Priya", 21)


p1.display()
p2.display()

#Question 6 
#  BankAccount Class hai. Isme constructor, methods aur object ka use ho raha hai.

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)


    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")


    def display(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)




account = BankAccount("Anu", 10000)


account.deposit(5000)
account.withdraw(3000)


account.display()

#Question 7 
#  Employee & Manager hai. Isme Inheritance + Constructor + super() ka use hua hai.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary




class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department


    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)




m1 = Manager("Rahul", 50000, "IT")


m1.display()

#Question 8 
#  Polymorphism hai. Isme Vehicle parent class hai aur Car aur Bike child classes hain.

class Vehicle:
    def start(self):
        print("Vehicle is starting")




class Car(Vehicle):
    def start(self):
        print("Car starts with a key")




class Bike(Vehicle):
    def start(self):
        print("Bike starts with a button")




car = Car()
bike = Bike()


car.start()
bike.start()

# Q9. Student — Grade Calculation
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 40:
            return "D"
        else:
            return "F"




s1 = Student("Rahul", 85)
s2 = Student("Priya", 72)
s3 = Student("Anu", 35)


print(s1.name, s1.calculate_grade())
print(s2.name, s2.calculate_grade())
print(s3.name, s3.calculate_grade())

# Q10. Shape — Circle and Rectangle
class Shape:
    def area(self):
        return 0




class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return 3.14 * self.radius * self.radius




class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def area(self):
        return self.length * self.width




shapes = [
    Circle(5),
    Rectangle(10, 5),
    Circle(3)
]


for shape in shapes:
    print("Area:", shape.area())


# Q11. Product — Total Price
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


    def total_price(self):
        return self.price * self.quantity




p1 = Product("Laptop", 50000, 1)
p2 = Product("Mouse", 500, 2)
p3 = Product("Keyboard", 1000, 3)


print(p1.name, "Total:", p1.total_price())
print(p2.name, "Total:", p2.total_price())
print(p3.name, "Total:", p3.total_price())


# Q12. Animal — Dog and Cat
class Animal:
    def __init__(self, name):
        self.name = name


    def sound(self):
        print("Animal makes a sound")




class Dog(Animal):
    def sound(self):
        print(self.name, "says Woof")




class Cat(Animal):
    def sound(self):
        print(self.name, "says Meow")




animals = [
    Dog("Tommy"),
    Cat("Kitty"),
    Dog("Bruno")
]


for animal in animals:
    animal.sound()


# Q13. Employee — Developer
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary




class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language


    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Programming Language:", self.programming_language)




d1 = Developer("Rahul", 50000, "Python")
d2 = Developer("Priya", 60000, "Java")


d1.display()
print()
d2.display()



# Q14. Person — Student and Teacher
class Person:
    def introduce(self):
        print("I am a person")




class Student(Person):
    def introduce(self):
        print("I am a student")




class Teacher(Person):
    def introduce(self):
        print("I am a teacher")




people = [
    Student(),
    Teacher(),
    Student()
]


for person in people:
    person.introduce()


# Q15. Book — EBook
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)




class EBook(Book):
    def __init__(self, title, author, price, file_size):
        super().__init__(title, author, price)
        self.file_size = file_size


    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("File Size:", self.file_size)




ebook = EBook(
    "Python Programming",
    "John",
    500,
    "5 MB"
)


ebook.display()

# Question 16 — Employee Management System hai.
class Employee:
    def __init__(self, name):
        self.name = name


    def work(self):
        print("Employee is working")




class Developer(Employee):
    def work(self):
        print(self.name, "is writing code")




class Designer(Employee):
    def work(self):
        print(self.name, "is designing UI")




class Manager(Employee):
    def work(self):
        print(self.name, "is managing the team")




employees = [
    Developer("Rahul"),
    Designer("Priya"),
    Manager("Anu")
]


for employee in employees:
    employee.work()

# Question 17 — Payment System 
class Payment:
    def __init__(self, amount):
        self.amount = amount


    def pay(self):
        pass




class UPI(Payment):
    def pay(self):
        print("Paid", self.amount, "using UPI")




class CreditCard(Payment):
    def pay(self):
        print("Paid", self.amount, "using Credit Card")




class NetBanking(Payment):
    def pay(self):
        print("Paid", self.amount, "using Net Banking")




payments = [
    UPI(500),
    CreditCard(1000),
    NetBanking(2000)
]


for payment in payments:
    payment.pay()

# Q18. School Management System
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)




class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course


    def display(self):
        print("Student:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)




class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject


    def display(self):
        print("Teacher:", self.name)
        print("Age:", self.age)
        print("Subject:", self.subject)




people = [
    Student("Rahul", 20, "B.Tech"),
    Teacher("Anu", 30, "Python")
]


for person in people:
    person.display()    

# Q19. Shape Hierarchy
class Shape:
    def area(self):
        pass




class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return 3.14 * self.radius * self.radius




class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def area(self):
        return self.length * self.width




class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height


    def area(self):
        return 0.5 * self.base * self.height




shapes = [
    Circle(5),
    Rectangle(10, 5),
    Triangle(10, 6)
]


for shape in shapes:
    print("Area:", shape.area())

# Q20. Banking System

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, amount):
        pass




class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Savings withdrawal successful")
        else:
            print("Insufficient balance")




class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.balance - 500:
            self.balance -= amount
            print("Current withdrawal successful")
        else:
            print("Withdrawal limit exceeded")




accounts = [
    SavingsAccount("Rahul", 10000),
    CurrentAccount("Anu", 10000)
]


for account in accounts:
    account.withdraw(2000)
    print("Name:", account.name)
    print("Balance:", account.balance)

# Q21. Complete Python Code

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


    def final_price(self):
        return self.price




class Electronics(Product):
    def final_price(self):
        return self.price * 1.10




class Clothing(Product):
    def final_price(self):
        return self.price * 1.05




class Grocery(Product):
    def final_price(self):
        return self.price * 0.95




products = [
    Electronics("Laptop", 50000),
    Clothing("Shirt", 2000),
    Grocery("Rice", 1000)
]


for product in products:
    print(product.name, "Final Price:", product.final_price())

# Q22. University Role System

class UniversityMember:
    def __init__(self, name):
        self.name = name


    def activity(self):
        pass




class Student(UniversityMember):
    def activity(self):
        print(self.name, "is attending classes")




class Professor(UniversityMember):
    def activity(self):
        print(self.name, "is teaching students")




class Researcher(UniversityMember):
    def activity(self):
        print(self.name, "is doing research")




members = [
    Student("Rahul"),
    Professor("Anu"),
    Researcher("Aman")
]


for member in members:
    member.activity()

# Question 23 — Transportation System
class Transport:
    def __init__(self, name):
        self.name = name


    def calculate_fare(self, distance):
        pass




class Bus(Transport):
    def calculate_fare(self, distance):
        return distance * 10




class Train(Transport):
    def calculate_fare(self, distance):
        return distance * 5




class Flight(Transport):
    def calculate_fare(self, distance):
        return distance * 20




transports = [
    Bus("Bus"),
    Train("Train"),
    Flight("Flight")
]


distance = 100


for transport in transports:
    print(transport.name, "Fare:", transport.calculate_fare(distance))

#Question 24 — Company Payroll System 

class Employee:
    def __init__(self, name):
        self.name = name


    def calculate_salary(self):
        pass




class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary


    def calculate_salary(self):
        return self.monthly_salary




class PartTimeEmployee(Employee):
    def __init__(self, name, hours, rate):
        super().__init__(name)
        self.hours = hours
        self.rate = rate


    def calculate_salary(self):
        return self.hours * self.rate




class Freelancer(Employee):
    def __init__(self, name, projects, payment):
        super().__init__(name)
        self.projects = projects
        self.payment = payment


    def calculate_salary(self):
        return self.projects * self.payment




employees = [
    FullTimeEmployee("Rahul", 50000),
    PartTimeEmployee("Anu", 80, 300),
    Freelancer("Aman", 4, 10000)
]


for employee in employees:
    print(
        employee.name,
        "Salary:",
        employee.calculate_salary()
    )

#Question 25 — Library Management System 
class LibraryItem:
    def __init__(self, title):
        self.title = title


    def borrow_period(self):
        pass




class Book(LibraryItem):
    def borrow_period(self):
        return 14




class Magazine(LibraryItem):
    def borrow_period(self):
        return 7




class DVD(LibraryItem):
    def borrow_period(self):
        return 5




items = [
    Book("Python Programming"),
    Magazine("Technology Today"),
    DVD("Inception")
]


for item in items:
    print(
        item.title,
        "can be borrowed for",
        item.borrow_period(),
        "days"
    )