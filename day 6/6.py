# n = int(input("Enter a number: "))
# for i in range(n):
#     for j in range(n):
#         if i == n - 1 or j == 0 or j == n - 1 or i == j or i + j == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n = int(input("Enter a number: "))
# for i in range(n):
#     for j in range(n):
#         if i == 0 and j < n-1 or j == 0 and i < n-1 :
#             print("* ", end="") 
#         else:
#             print(" ", end="")
#     print()

# n = 5
# for i in range(n):
#     for j in range(10):
#         if (i == 0 and j % 2 == 0 and j < 8) or (i == 1 and j in [0,4]) or (i == 2 and j in [0,2,6]) or (i == 3 and j in [0,4,8]) or (i == 4 and j == 6):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# n = int(input("Enter a number: "))
# for i in range(n):
#     for j in range(n):
#         if (i == 0 or i == n - 1 ):
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()

# n = int(input("Enter a number: "))
# for i in range(n):
#     for j in range(n):
#         if(i == 0 or j == 0 or i == n - 1):
#             if(i + j == 0 or j == 0 and i == n - 1):
#                 print(" ", end=" ")
#             else:
#                 print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

h = 8
b = h // 2 + 2
for i in range(h + 1):
    for j in range(b):
        if(j == 0 or i == 0 and j <= b // 2 
           or j - i == b // 2 
           or i == 4 and j < b - 2 
           or i + j == b + 1 and i < b - 1
           or i == b - 1 and j == b - 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
