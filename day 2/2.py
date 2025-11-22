# a = 51
# b = a
# a = a % 10  # 1
# b = b // 10  # 5
# print(a * 10 + b)

# a = 15
# print(a % 2 == 0)

# int to float, str, bool, complex
# a = 5
# print(float(a))      # 5.0
# print(str(a))        # '5'
# print(bool(a))       # True
# print(complex(a))    # (5+0j)
# print("*" * 20)
# float to int, str, bool, complex
# b = 3.14
# print(int(b))        # 3
# print(str(b))        # '3.14'
# print(bool(b))       # True
# print(complex(b))    # (3.14+0j)
# print("*" * 20)
# str to int, float, bool, complex
# c = "42"
# print(int(c))        # 42
# print(float(c))      # 42.0
# print(bool(c))       # True
# print(complex(c))    # (42+0j)
# print("*" * 20)
# bool to int, float, str, complex
# d = False
# print(int(d))        # 0
# print(float(d))      # 0.0
# print(str(d))        # 'False'
# print(complex(d))    # 0j
# print("*" * 20)
# complex to str, bool
# e = 2 + 3j
# print(str(e))        # '(2+3j)'
# print(bool(e))       # True
# print("*" * 20)
# list to tuple, set, str
# lst = [1, 2, 3]
# print(tuple(lst))    # (1, 2, 3)
# print(set(lst))      # {1, 2, 3}
# print(str(lst))      # '[1, 2, 3]'
# print("*" * 20)
# tuple to list, set, str
# tup = (4, 5, 6)
# print(list(tup))     # [4, 5, 6]
# print(set(tup))      # {4, 5, 6}
# print(str(tup))      # '(4, 5, 6)'
# print("*" * 20)
# set to list, tuple, str
# s = {7, 8, 9}
# print(list(s))       # [8, 9, 7] (order may vary)
# print(tuple(s))      # (8, 9, 7) (order may vary)
# print(str(s))        # '{8, 9, 7}'
# print("*" * 20)
# list of tuples to dict
# pairs = [("a", 1), ("b", 2)]
# print(dict(pairs))   # {'a': 1, 'b': 2}
# print("*" * 20)
# dict to list, tuple, set (keys only)
# dct = {'x': 10, 'y': 20}
# print(list(dct))     # ['x', 'y']
# print(tuple(dct))    # ('x', 'y')
# print(set(dct))      # {'x', 'y'}
# print("*" * 20)
# zip to list, tuple, set
# l1 = [1, 2]
# l2 = ['a', 'b']
# z = zip(l1, l2)
# print(list(z))       # [(1, 'a'), (2, 'b')]
# z = zip(l1, l2)
# print(tuple(z))      # ((1, 'a'), (2, 'b'))
# z = zip(l1, l2)
# print(set(z))        # {(1, 'a'), (2, 'b')}
# print("*" * 20)

# x , y = map(int, input().split())
# operation = input()
# if operation == "+":
#     print(x + y)
# elif operation == "-":
#     print(x - y)
# elif operation == "*":
#     print(x * y)
# elif operation == "/":
#     if y != 0:
#         print(x / y)
#     else:
#         print("Division by zero is not possible.")
# elif operation == "//":
#     if y != 0:
#         print(x // y)
#     else:
#         print("Division by zero is not possible.")
# elif operation == "%":
#     if y != 0:
#         print(x % y)
#     else:
#         print("Division by zero is not possible.")
# elif operation == "**":
#     print(x ** y)
# else:
#     print("Unknown operation")

name = input("Enter your name: ")
password = input("Enter your password: ")
x = int(input("press 1 for login \npress 2 for exit\npress 3 for reset password\n"))
if x == 1:
    name1 = input("Enter your name: ")
    password1 = input("Enter your password: ")
    if name == name1 and password == password1:
        print("You are logged in")
    else:
        print("Invalid name or password")
elif x == 2:
    print("You are exited")
elif x == 3:
    print("Reset your password")
    password2 = input("Enter your old password: ")
    if(password2 == password):
        new_password = input("Enter your new password: ")
        if(new_password != password):
            password = new_password
            print("Your password has been changed")
        else:
            print("Your new password must be different from the old one")
    else:
        print("Invalid password")
else:
    print("Invalid input")