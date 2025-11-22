# n = 5
# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end=" ")
#     val = 1
#     for j in range(i + 1):
#         print(val, end="   ")
#         val = val * (i - j) // (j + 1)
#     print()

# n = int(input("Enter a number: "))
# for i in range(n):
#     for j in range(i + 1):
#         print(n, end=" ")
#     n += 1
#     print()

# n = int(input("Enter the last number: "))
# row = int(input("Enter numbers per row: "))

# for i in range(1, n + 1, row):   # row-wise loop
#     if (i // row) % 2 == 0:  # even row (0,2,4..)
#         for j in range(i, i + row):
#             if j <= n:
#                 print(j, end=" ")
#     else:  # odd row (1,3,5..)
#         for j in range(i + row - 1, i - 1, -1):
#             if j <= n:
#                 print(j, end=" ")
#         print()

# Snake board pattern using 2D list

# data = [[1, 2, 3, 4, 5],
#         [6, 7, 8, 9, 10],
#         [11, 12, 13, 14, 15],
#         [16, 17, 18, 19, 20],
#         [21, 22, 23, 24, 25]]

# n = len(data)
# m = len(data[0])

# for i in range(n):
#     if i % 2 == 0:
#         print(*data[i])        
#     else:
#         print(*data[i][::-1])

arr = [2, 7, 11, 15]
total = 9
d = {}
for i in range(len(arr)):
    x = total - arr[i]
    if x in d:
        print([d[x], i])
    d[arr[i]] = i