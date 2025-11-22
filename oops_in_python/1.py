# class and object 
"""we describe method in a class and call that method using object of that class"""

# class Person:
#     def greet(self):
#         print("Hello")
# p1 = Person()
# p1.greet()

# class student:
#     def records(self, subject, marks):
#         self.sub = subject
#         self.no = marks
# mohan = student()
# mohan.records("maths", 90)

# sohan = student()
# sohan.records("science", 80)

# sohan.sub = "english"# changing attribute value from outside the class

# data = f'''Hello,
# Here are the student records:
# Mohan - Subject: {mohan.sub}, Marks: {mohan.no}
# Sohan - Subject: {sohan.sub}, Marks: {sohan.no}'''

# print(data)

''' practice problem 1 : there is a real world scenario. You have to create the attributes and method to it. 
Take the example of your college.'''

# class College:
#     def jit(self,name,cgpa):
#         self.name = name
#         self.clg_name = "Jawaharlal Institute of Technology, Borawan"
#         self.branch = "CSE with specialisation in Artificial Intelligence and Machine Learning"
#         self.year = 3
#         self.cgpa = cgpa
# clg = College()
# clg.jit("Chinmay Joshi",7.24)

# data = f'''Hello,
# My name is Chinmay Joshi.
# I am studying in {clg.clg_name} college.
# I am in {clg.year} year of my graduation.
# My branch is {clg.branch}.
# My CGPA is {clg.cgpa}.
# I am proud to be a student of {clg.clg_name}.'''

# print(data)

# class c1:
#     data = 90
#     def m1(self):
#         pass
# c1.new_data = "values added"
# obj = c1()
# print(obj.data,c1.data,obj.new_data,c1.new_data)

# class c1:
#     a = 10
#     def m1(self):
#         print(c1.a)
#         c1.b=100
#         c1.a+=10
#         print(c1.a)
#         c1.b+=100
#         self.a+=50
#         print(self.a)
#         print(c1.b)
# obj = c1()
# obj.m1()

# class c1:
#     a = 10
#     @classmethod
#     def m1(cls):
#         print(cls.a)
#         cls.a+=10
#         print(cls.a)
#         cls.myvar = 50
# obj = c1()
# obj.m1()
# print(c1.myvar)

# class c1:
#     a = 10
#     @classmethod
#     def m2(cls):
#         print(cls.a)

# @c1
# def m1(cls):
#         cls.a+=1
#         print(cls.a)
# obj = c1()
# obj.m1()

"""Constructor in python (__init__)"""
# dunder methods : __init__, __str__, __repr__, __add__, __len__

# class c1:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# x = input("Enter your name: ")
# y = int(input("Enter your age: "))
# obj = c1(x,y)
# print(obj.name,'\n',obj.age)

"""Distructor in python (__del__)"""

# class c1:
#     def __init__(self):
#         print("Object is created")
#     def __del__(self):
#         print("Object is destroyed")
# obj = c1()
# del obj

# class c1:
#     data = 90
#     def m1(self):
#         print("i am m1")
# obj = c1()
# del c1.data
# print(obj.data)

# Encapsulation in python
"""we can restrict access to methods and variables. This prevents data from direct modification which is called encapsulation.
In python we denote private attribute using underscore(_)"""

""" __ -> private member
    _  -> protected member
    no underscore -> public member 
"""


"""Example of constructor"""
# class c1:
#     def __init__(self,a):
#         self.a = a
# obj = c1(90)
# print(obj.a)

# class c1:
#     def __init__(self):
#         print("first constructor")
#     def __init__(self):
#         print("second constructor")
# obj = c1()

"""same for methods, last one will be considered"""

"""Abstraction in python"""
"""Abstraction is the process of hiding the real implementation of an application from the user and emphasizing only on usage of it.
In python we can achieve abstraction using abstract class and method from abc module"""

# from abc import ABC, abstractmethod

# class c1(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
# class c2(c1):
#     def m1(self):
#         print("implementation of abstract method")
# obj = c2()
# obj.m1()

"""Inheritance in python"""
"""Inheritance is a way of creating a new class for using details of an existing class without modifying it.
The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).""" 


""" types of inheritance:
1. Single Inheritance
2. Multilevel Inheritance
3. Hierarchical Inheritance
4. Multiple Inheritance
5. Hybrid Inheritance
"""

"""
Single Inheritance : when a child class inherits from a single parent class 
example : 
class Parent:
    print("This is parent class")
class Child(Parent):
    print("This is child class")

obj = Child()
obj will have access to all the properties and methods of Parent class.

"""


"""
Multilevel Inheritance : when a child class inherits from a parent class, and then another class inherits from that child class.
example :
class GrandParent:
    print("This is grandparent class")
class Parent(GrandParent):
    print("This is parent class")
class Child(Parent):
    print("This is child class")

obj = Child()
obj will have access to all the properties and methods of Parent and GrandParent classes.
"""


"""
Hierarchical Inheritance : when multiple child classes inherit from a single parent class.
example :
class Parent:
    print("This is parent class")
class Child1(Parent):
    print("This is child1 class")
class Child2(Parent):
    print("This is child2 class")

obj1 = Child1()
obj2 = Child2()
obj1 and obj2 will have access to all the properties and methods of Parent class.
"""


"""
Multiple Inheritance : when a child class inherits from multiple parent classes.
example :
class Parent1:
    print("This is parent1 class")
class Parent2:
    print("This is parent2 class")
class Child(Parent1, Parent2):
    print("This is child class")

obj = Child()
obj will have access to all the properties and methods of Parent1 and Parent2 classes.
"""


"""
Hybrid Inheritance : when a combination of two or more types of inheritance is used.
example :
class GrandParent:
    print("This is grandparent class")
class Parent1(GrandParent):
    print("This is parent1 class")
class Parent2(GrandParent):
    print("This is parent2 class")
class Child(Parent1, Parent2):
    print("This is child class")

obj = Child()
obj will have access to all the properties and methods of Parent1, Parent2 and GrandParent
"""


"""examples of inheritance in python"""


# class Parent:
#     def func1(self):
#         print("This function is in parent class.")

# class Child(Parent):
#     def func2(self):
#         print("This function is in child class.")

# object = Child()
# object.func1()
# object.func2()

# class GrandParent:
#     def func1(self):
#         print("This function is in grandparent class.")
# class Parent(GrandParent):
#     def func2(self):
#         print("This function is in parent class.")
# class Child(Parent):
#     def func3(self):
#         print("This function is in child class.")
# object = Child()
# object.func1()
# object.func2()
# object.func3()

# class A:
#     def func1(self):
#         print("This function is in class A.")
# class B:
#     def func2(self):
#         print("This function is in class B.")
# class C(A, B):
#     def func3(self):
#         print("This function is in class C.")
# object = C()
# object.func1()
# object.func2()
# object.func3()

# class A:
#     def func1(self):
#         print("This function is in class A.")
# class B(A):
#     def func2(self):
#         print("This function is in class B.")
# class C(A):
#     def func3(self):
#         print("This function is in class C.")
# class D(B, C):
#     def func4(self):
#         print("This function is in class D.")
# object = D()
# object.func1()
# object.func2()
# object.func3()
# object.func4()

# print(D.mro())  # method resolution order
# print(D.__mro__)
# print(help(D))


"""Polymorphism in python"""

"""Polymorphism means having many forms. In programming, polymorphism means the same function name (but different signatures) being used for different types.
The key difference is the data types and number of arguments used in function."""

# class India:
#     def capital(self):
#         print("New Delhi is the capital of India.")
#     def language(self):
#         print("Hindi is the most widely spoken language of India.")
#     def type(self):
#         print("India is a developing country.")
# class USA:
#     def capital(self):
#         print("Washington, D.C. is the capital of USA.")
#     def language(self):
#         print("English is the primary language of USA.")
#     def type(self):
#         print("USA is a developed country.")
# obj_ind = India()
# obj_usa = USA()
# for country in (obj_ind, obj_usa):
#     country.capital()
#     country.language()
#     country.type()
# def add(x, y, z=0):
#     return x + y + z
# print(add(2, 3))
# print(add(2, 3, 4))
# print(add("Hello, ", "world!"))
# print(add([1, 2], [3, 4]))
# print(add((1, 2), (3, 4)))
# class c1:
#     def add(self, a, b):
#         return a + b
# obj = c1()
# print(obj.add(2, 3))
# print(obj.add("Hello, ", "world!"))
# print(obj.add([1, 2], [3, 4]))
# print(obj.add((1, 2), (3, 4)))