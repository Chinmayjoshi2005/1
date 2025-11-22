"""yeild"""

# def f1():
#     print("start")
#     yield 1
#     print("continue")
#     yield 2
#     print("end")
#     yield 3
# a = f1()
# print(next(a))
# print(next(a))
# print(next(a))


# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1
# for i in countdown(3):
#     print(i)

# def f1():
#     for i in range(4):
#         yield i
# a = f1()
# for i in f1():
#     print(next(a))

# def f1(n):
#     for i in range(n):
#         yield i

# for i in f1(4):
#     print(i)

"""Decorators"""

# def display(fun):
#     def wrapper():
#         print("Before function call")
#         fun()
#         print("After function call")
#     return wrapper
# @display
# def f1():
#     print("Inside function")
# f1()

# def multiply(fun):
#     def wrapper(x, y):
#         fun(x, y)
#         print("Multiplication : ",x * y)
#     return wrapper
# @multiply
# def add(a, b):
#     print("Addition : ",a + b)
# add(2, 3)

# def f1():
#     a = 10
#     def f2():
#         a = 90
#     f2()
#     return a
# print(f1())

