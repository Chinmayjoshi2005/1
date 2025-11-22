# data = [1,2,3,4]
# def fn():
#     print(data[::-1])
# fn()

# def table(num):
#     for i in range(1,11):
#         print(f"{num} * {i} = {num*i}")
# # a = int(input("Enter a number : "))
# table(int(input("Enter a number : ")))

# def fn(word):
#     for i in range(len(word)-1,-1,-1):
#         print(word[i],end="")
# fn(input("Enter a word : "))

# def fabonaci(n):
#     a, b = n, n+1
#     data = [a, b]
#     for i in range(2, 10):
#         c = a + b
#         data.append(c)
#         a, b = b, c
#     return data

# print(fabonaci(int(input("Enter a number from where you need to start the fabonaci series : "))))

# def f1(n):
#     n += 1
#     return n
# print(f1(9))

# def f2():
#     n = 10
# print(f2())

# def f3(n):
#     n += 1
# print(f3(10))

# def f4():
#     n = 10
#     return n
# print(f4())

# data = [1,2,3,4,5]
# for i in range:
#     print(i)

# data = [f"{'*' * i}{i}{'*' * i}" for i in range(1, 4)]
# print(data)

# data = [x for x in range(1,21) if x % 2 == 0]
# print(data)

# data = [x for x in range (1,11) if x > 0 and x % 2 == 0]
# print(data)

# n = int(input("Enter a number : "))
# data = [f"{n} * {i} = {n * i}"for i in range (1,11) ]
# print(data , end = '')

# data = [f'{'*'*i}{i}{'*'*i}' for i in range(1,4)]
# print(data)

# data = [(x,y) for x in range(1,5) for y in range(1,3)]
# print(data)

data = [(lambda x : x** 2)(x) for x in range(1,11)]
print(data)