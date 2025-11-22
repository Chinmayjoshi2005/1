# for i in range (5):
#     for j in range(3):
#         print("* " , end='')
#     print()

# for i in range(4):
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()

# *
# * *
# * * *
# * * * *

# for i in range(4):
#     for j in range(4 - i):
#         print("*" , end=" ")
#     print()

# * * * *
# * * *
# * *
# *

# for i in range(5):
#     for j in range(5):
#         if i == 4 or j == 0 or j == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n = int(input("enter : "))
# for i in range(n):
#     for j in range(n):
#         if i == n - 1 or j == 0 or j == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# * * * * * * * * * *
# * *             * *
# *   *        *    *
# *     *    *      *
# *       * *       *
# *       * *       *
# *     *    *      *
# *   *        *    *
# * *             * *
# * * * * * * * * * *

# n = int(input("Enter even n (>=4): "))
# for i in range(n):
#     for j in range(n):
#         if (i == 0 or i == n - 1 or j == 0 or j == n - 1 or i + j == n - 1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# n = int(input("enter the size of diamond : "))
# for i in range(n):
#     print(" " * (n - i - 1), end="") 
#     print("*", end="")  
#     if i > 0:
#         print(" " * (2 * i - 1), end="")  
#         print("*", end="")  
#     print() 
# for i in range(n - 2, -1, -1):
#     print(" " * (n - i - 1), end="")
#     print("*", end="")
#     if i > 0:
#         print(" " * (2 * i - 1), end="")
#         print("*", end="")
#     print()

# for i in range(5):
#     for _ in range(5-i):
#         print(" " , end = ' ')
#     for _ in range (i + 1) :
#         print ("*" , end =" ")
#     for _ in range (i) :
#         print ("*" , end =" ")
#     print ()  


# n = int(input("Enter size : "))
# for i in range(n,-1,-1):
#     for _ in range(n-i):
#         print(" " , end = ' ')
#     for _ in range (i + 1) :
#         print ("*" , end =" ")
#     for _ in range (i) :
#         print ("*" , end =" ")
#     print ()

# n = int(input("Enter size : "))
# for i in range(n):
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()
# for i in range(0,n + 1):
#     print("*", end=" ")
# print()
# for i in range(n):
#     for j in range(n - i):
#         print("*" , end=" ")
#     print()

