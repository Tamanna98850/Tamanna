 # 10 Practice Questions with Solutions
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

