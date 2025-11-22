#1. Print a hollow diamond pattern of stars (n=5). 
#Ans :-
'''
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
'''

'''
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
'''

#2. Pascal's Triangle (n=5).
#Ans :-
'''
n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    val = 1
    for j in range(i + 1):
        print(val, end="   ")
        val = val * (i - j) // (j + 1)
    print()
'''

'''
        1   
      1   1   
    1   2   1   
  1   3   3   1   
1   4   6   4   1   

'''

#3. Floyd's Triangle reverse aligned (n=5).
#Ans :-
'''
n = 5
num = n * (n + 1) // 2
for i in range(n, 0, -1):
    for j in range(i):
        print(num, end=" ")
        num -= 1
    print()
'''

'''
15 14 13 12 11 
10 9 8 7 
6 5 4 
3 2 
1 
'''

#
#

# n = 5
# for i in range(1, n + 1):
#     for j in range(i):
#         print("*", end="")
#     for j in range(2 * (n - i)):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end="")
#     print()

# for i in range(n - 1, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     for j in range(2 * (n - i)):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end="")
#     print()