### Python OOP – Remaining Topics
### Notes with Examples, Solutions and Outputs
### Topics covered: Public, Protected, Private, Name Mangling, Class Variables, Instance Variables, super(), Types of Inheritance, MRO, object class, Dunder Methods, Operator Overloading, Composition, Aggregation and Association.

# 1. Public Members
# Concept: Public members can be accessed from outside the class normally.
# Example / Solution:
class Student:
    def __init__(self, name):
        self.name = name

student = Student("Anushka")
print(student.name)

# 2. Protected Members
# Concept: A single underscore (_) indicates a protected member by convention. It is intended mainly for use inside the class and its child classes, but Python does not strictly block access.
# Example / Solution:
class Student:
    def __init__(self):
        self._course = "Python"

class Child(Student):
    def show(self):
        print(self._course)

obj = Child()
obj.show()

# 3. Private Members
# Concept: A double underscore (__) is used for a private member. Python applies name mangling, so direct access using the original name normally fails.
# Example / Solution:
class Student:
    def __init__(self):
        self.__marks = 90

    def show_marks(self):
        print(self.__marks)

student = Student()
student.show_marks()

# 4. Name Mangling
# Concept: Python changes a private attribute such as __marks to a name similar to _Student__marks internally. This helps avoid accidental access and name conflicts; it is not true security.
# Example / Solution:
class Student:
    def __init__(self):
        self.__marks = 90

student = Student()
print(student._Student__marks)

# 5. Class Variables
# Concept: A class variable belongs to the class and is shared by instances unless an instance creates its own attribute with the same name.
# Example / Solution:
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

s1 = Student("Anushka")
s2 = Student("Rahul")

print(s1.school)
print(s2.school)

# 6. Instance Variables
# Concept: Instance variables belong to individual objects. Different objects can store different values.
# Example / Solution:
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Anushka", 23)
s2 = Student("Rahul", 22)

print(s1.name, s1.age)
print(s2.name, s2.age)

# 7. super()
# Concept: super() is used to access parent-class methods from a child class.
# Example / Solution:
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")

dog = Dog()
dog.sound()

# 8. super() with Constructor
# Concept: super().__init__() allows a child class to reuse the parent's constructor instead of repeating the same initialization code.
# Example / Solution:
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

student = Student("Anushka", "Python")

print(student.name)
print(student.course)

# 9. Single Inheritance
# Concept: One parent class is inherited by one child class.
# Example / Solution:
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

dog = Dog()
dog.eat()
dog.bark()

# 10. Multilevel Inheritance
# Concept: Inheritance continues through multiple levels: Grandparent → Parent → Child.
# Example / Solution:
class Animal:
    def eat(self):
        print("Eating")

class Mammal(Animal):
    def walk(self):
        print("Walking")

class Dog(Mammal):
    def bark(self):
        print("Barking")

dog = Dog()
dog.eat()
dog.walk()
dog.bark()

# 11. Multiple Inheritance
# Concept: One child class inherits from more than one parent class.
# Example / Solution:
class Father:
    def skills(self):
        print("Driving")

class Mother:
    def talent(self):
        print("Cooking")

class Child(Father, Mother):
    pass

child = Child()
child.skills()
child.talent()

# 12. Hierarchical Inheritance
# Concept: One parent class is inherited by multiple child classes.
# Example / Solution:
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

class Cat(Animal):
    def meow(self):
        print("Meowing")

dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()

# 13. Hybrid Inheritance
# Concept: Hybrid inheritance combines two or more inheritance patterns.
# Example / Solution:
class A:
    def show_a(self):
        print("A")

class B(A):
    def show_b(self):
        print("B")

class C(A):
    def show_c(self):
        print("C")

class D(B, C):
    def show_d(self):
        print("D")

obj = D()
obj.show_a()
obj.show_b()
obj.show_c()
obj.show_d()

# 14. MRO – Method Resolution Order
# Concept: MRO tells Python the order in which it searches classes for a method, especially in multiple inheritance.
# Example / Solution:
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

obj = D()
obj.show()

print([cls.__name__ for cls in D.mro()])

# 15. object Class
# Concept: object is the ultimate base class for normal Python classes. Classes inherit built-in behavior from it.
# Example / Solution:
class Student:
    pass

print(Student.__bases__)

# 16. __str__() Dunder Method
# Concept: __str__() controls the user-friendly string representation of an object when print() is used.
# Example / Solution:
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

student = Student("Anushka")
print(student)

# 17. __len__() Dunder Method
# Concept: __len__() allows an object to work with Python's len() function.
# Example / Solution:
class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

team = Team(["A", "B", "C"])
print(len(team))

# 18. __add__() and Operator Overloading
# Concept: Operator overloading allows operators such as + to be given custom behavior for objects.
# Example / Solution:
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

a = Number(10)
b = Number(20)

print(a + b)

# 19. __eq__() Operator Overloading
# Concept: __eq__() controls how == behaves when comparing two objects.
# Example / Solution:
class Student:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

s1 = Student("Anushka")
s2 = Student("Anushka")

print(s1 == s2)

# 20. __lt__() and __gt__()
# Concept: __lt__() controls < and __gt__() controls > for custom objects.
# Example / Solution:
class Student:
    def __init__(self, marks):
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

s1 = Student(90)
s2 = Student(75)

print(s1 > s2)

# 21. Composition
# Concept: Composition represents a strong HAS-A relationship. A Car can contain an Engine object.
# Example / Solution:
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

car = Car()
car.start()

# 22. Aggregation
# Concept: Aggregation is a HAS-A relationship where the contained object can exist independently of the container.
# Example / Solution:
class Teacher:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, teacher):
        self.teacher = teacher

teacher = Teacher("Rahul")
department = Department(teacher)

print(department.teacher.name)
print(teacher.name)

# 23. Association
# Concept: Association means two objects are related or interact with each other, without necessarily owning each other.
# Example / Solution:
class Student:
    def __init__(self, name):
        self.name = name

class Teacher:
    def teach(self, student):
        print("Teaching", student.name)

student = Student("Anushka")
teacher = Teacher()

teacher.teach(student)

