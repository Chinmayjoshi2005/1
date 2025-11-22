# a = 'apple'
# b = 'apple'
# print(id(a))
# print(id(b))

# print(bin(12&15))
# print(12&15)

# data = [1, 2, 3, 4, 5]
# l = []
# for i in data:
#     print(i**2)
#     if(i % 2 == 0):
#         l.append(i)
# print("Even numbers : ", l)

# data = 'welcome to jit'
# for i in data:
#     print(i, end="")
#     if(i == ' '):
#         print()

# data = {"A" : 1, "B"  : 2, "C" : 3}
# for i in data:
#     print(i)
#     print(i, '--', data[i])

# for i in range(1,10):
#     print(i)

# x = int(input("Enter a number : "))
# for i in range(1, 11):
#     print(x, 'x', i, '=', x*i)

# x, y = map(int, input("Enter range : ").split())
# for i in range(x, y+1):
#     if(i % 2 == 0):
#         print(i)

for num in range(1, 11):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)