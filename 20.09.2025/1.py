# while loop 

# n = 20
# while n >= 2:
#     if n == 10:
#         n -= 2
#         continue
#     print(n)
#     n -= 2

# n = int(input("Enter a number: "))
# m = int(input("Enter a number: "))

# while n < m:
#     if(n % 3 == 0 or n % 5 == 0):
#         print(n)

# n = int(input("Enter a number: "))
# i = 2
# check = True
# while i < n:
#     if n % i == 0:
#         check = False
#         break
#     i += 1
# if check:
#     print(f"{n} is prime number")
# else:
#     print(f"{n} is not prime number")

# galat hai upper vala 

# n = int(input("Enter a number: "))
# check = True
# for i in range(2,n):
#     if(n % i == 0):
#         check = False
#         break
# if(check):
#     print(f"{n} is prime number")
# else:
#     print(f"{n} is not prime number")

# data  = "123ABC456"
# print(data.isalnum())
# print(data.rfind("l"))
# print(data.isdigit())

# i = len(data) - 1
# while i >= 0 :
#     if data[i].isdigit():
#         print(data[i], end="")
#     i -= 1


# data = 'aaabbbcgggyyyssshh'
# print("data = 'aaabbbcgggyyyssshh'")
# x = input("Enter a single character from above list to count: ")
# if x == 'a':
#     print("a =",data.count('a'))
# elif x == 'b':
#     print("b =",data.count('b'))
# elif x == 'c':
#     print("c =",data.count('c'))
# elif x == 'g':
#     print("g =",data.count('g'))
# elif x == 'y':
#     print("y =",data.count('y'))
# elif x == 's':
#     print("s =",data.count('s'))
# elif x == 'h':
#     print("h =",data.count('h'))
# else:
#     print("Invalid input")

# import tkinter as tk
# window = tk.Tk()
# window.geometry("700*500")
# window.config(bg='pink')
# lable = tk.lable(window, text = 'fuck u', font = ('bold', 25) background)

# data = [3,5,7,9,25,7]
# new = []
# result = []
# for i in range(len(data)):
#     if data[i] == data[i - 1] + 1:
#         new.append(data[i])
#     else:
#         result.append(new)
#         new = [data[i]]
# result.append(new)
# result.pop(0)
# print(result)

# data = [1,2,3,4,8,9,10]
# new = []
# result = []
# for i in range(len(data)):
#     if data[i - 1] + 1 == data[i]:
#         new.append(data[i])
#     else:
#         result.append(new)
#         new = [data[i]]
# result.append(new)

# print(result)


data = [1,2,3,4,8,9,10]
# data.extend(11)
print(data)