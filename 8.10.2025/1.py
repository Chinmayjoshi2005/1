# def recur(n):
#     if n <= 0:
#         return 1
#     else:
#         return(print(n), recur(n-1))
    
# recur(10)


# list = [123,34,5,5,67,65,34,123]
# unique=[]
# def recur(x,list):
#     if x == len(list):
#         return 
#     print(list[x])
#     return recur(x+1,list)
# recur(0,list)

# def recur(x,list):
#     if x == len(list):
#         return
#     elif list[x] not in unique:
#         unique.append(list[x])
#         return recur(x+1,list)
#     else:
#         return recur(x+1,list)
# recur(0,list)
# print(unique)

# map 

# def square(a):
#     return a*a
# data = [2,3,4,5]
# new = list(map(square,data))
# print(new)
# output = [4,9,16,25]

# data = map(int,input().split())
# print(data)

# def filter_even(n):
#     return n%2==0
# new = list(filter(filter_even,[12,23,3,3,45,56,7]))
# print(new)

# def filter_data(n, data):
#     if not data:
#         return []
#     head, *tail = data
#     if len(head) <= n:
#         return [head] + filter_data(n, tail)
#     else:
#         return filter_data(n, tail)

# data = ['cat', 'alpha', 'dog', 'beta', 'rat']
# result = filter_data(3, data)
# print(result)

# wap to check a number is a strong number or not
# wap to print star pattern
#1.
# * * * * * * * * * *
# * *             * *
# *   *         *   *
# *     *     *     *
# *       * *       *
# *       * *       *
# *     *     *     *
# *   *         *   *
# * *             * *
# * * * * * * * * * *

#2.
#       *
#      * *
#     * * *
#    * * * *
#   * * * * *
#  * * * * * *
# * * * * * * *

#3.pascals triangle pattern.

