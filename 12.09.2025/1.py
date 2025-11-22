# n = 5
# a = 1
# for i in range(n):
#     for  j in range(n):
#         print(a, end=" ")
#         a += 1

# data = [[1, 2, 3, 4, 5],
#         [6, 7, 8, 9, 10],
#         [11, 12, 13, 14, 15],
#         [16, 17, 18, 190],
#         [21, 22, 23, 24, 25]]
# n = len(data)

# itr = []

# for i in range(n):
#     for j in range(n):
#         if i == 0 :
#             itr.append(data[i][j])
#         elif j == n - 1:
#             itr.append(data[i][j])
#         elif i == n - 1 or j == 0 and i == n - 1:
#             itr.append(data[i][n - j - 1])
#         elif j == 0 and i > 0:
#             itr.append(data[n - i - 1][j])

# print(itr)