# PRACTICE SET 1

# 1. Define a function that prints your name.
def my_name():
    print("Chinu")

# output : Chinu

# 2. Define a function that takes two numbers and prints their sum.
def add_numbers(a, b):
    print("Sum:", a + b)

add_numbers(5, 10)

# output : Sum: 15

# 3. What keyword is used to define a function in Python?
# Answer: The keyword used is 'def'.


# 4. Write a function to calculate the area of a rectangle (length, width).
def area_rectangle(length, width):
    area = length * width
    print("Area of rectangle:", area)

area_rectangle(5, 10)

# output : Area of rectangle: 50

# 5. Write a function welcome(name="Guest") that prints a welcome message.
def welcome(name="Guest"):
    print("Welcome,", name)

welcome()

# output : Welcome, Guest



# 6. What happens if you pass fewer or more positional arguments?
# Answer:
# Fewer arguments → TypeError (missing positional argument)
# More arguments  → TypeError (too many positional arguments)


# 7. Program showing local and global variables with same name.
x = 10  # global variable
def show():
    x = 5  # local variable
    print("Inside function:", x)
show()
print("Outside function:", x)

# output : Inside function: 5
#          Outside function: 10


# 8. How can you modify a global variable inside a function?
# Answer: Use the 'global' keyword.
count = 0
def modify():
    global count
    count += 1
    print("Inside function:", count)
modify()
print("Outside function:", count)

# output : Inside function: 1
#          Outside function: 1


# 9. What happens if you try to access a local variable outside a function?
# Answer: It gives NameError (variable not defined outside function scope)


# 10. Write a function that returns the product of two numbers.
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print("Product is:", result)

# output : Product is: 20

# 11. Create a function that returns both sum and difference of two numbers.
def sum_and_diff(a, b):
    return a + b, a - b
result = sum_and_diff(10, 5)
print("Sum and Difference:", result)

# output : Sum and Difference: (15, 5)


# 12. What will happen if a function has no return statement?
# Answer: It automatically returns 'None'.


# 13. Write a function outer() that defines and calls an inner() function.
def outer():
    print("Outer function")
    def inner():
        print("Inner function")
    inner()
outer()

# output : Outer function
#          Inner function

# 14. Program where one function calls another function inside it.
def greet():
    print("Hello!")
def welcome():
    greet()
    print("Welcome to My Paradise!")
welcome()

# output : Hello!
#          Welcome to Python!

# 15. Create a function that returns the square of the sum of two numbers using another function.
def add(a, b):
    return a + b
def square_of_sum(x, y):
    return add(x, y) ** 2
print("Square of sum:", square_of_sum(10, 5))

# output : Square of sum: 225

# 16. Store a function’s return value in a variable and print it.
def cube(n):
    return n ** 3
result = cube(4)
print("Cube is:", result)

# output : Cube is: 64

# 17. Pass a variable (that stores function result) to another function.
def double(n):
    return n * 2
def show_value(value):
    print("Value is:", value)
res = double(5)
show_value(res)

# output : Value is: 10

# 18. Can a function call another function in its return statement?
# Answer: Yes, a function can call another function in its return.
def square(n):
    return n * n
def cube(n):
    return n * square(n)
print("Cube:", cube(3))

# output : Cube: 27

# 19. Write one example each of:
# • Function with no parameter
# • Function with parameter
# • Function with default value
# • Function with return
# • Function without return

# Function with no parameter
def say_hello():
    print("Hello!")

# Function with parameter
def greet_person(name):
    print("Hello,", name)

# Function with default value
def welcome_user(name="Guest"):
    print("Welcome,", name)

# Function with return
def add_nums(a, b):
    return a + b

# Function without return
def subtract_nums(a, b):
    print("Difference:", a - b)

# 20. Explain the relationship between default and local argument values with example.
# Answer:
# If a function has a default value but a local value is passed, 
# then the local value overrides the default one.

def greet_example(name="Guest"):
    print("Hello,", name)

greet_example()        # uses default "Guest"
greet_example("Chinu") # overrides default

# output : Hello, Guest
#          Hello, Chinu


# Q1.
def greet():
    print("Hello, welcome to Python!")
greet()
# Output:
# Hello, welcome to Python!

# Q2.
def add(a, b):
    print("Sum is:", a + b)
add(10, 20)
# Output:
# Sum is: 30

# Q3.
def greet(name="User"):
    print("Hello,", name)
greet()
greet("Great Chinu")
# Output:
# Hello, User
# Hello, Great Chinu

# Q4.
x = 10  # global
def show():
    y = 5  # local
    print("Inside:", x, y)
show()
print("Outside:", x)
# Output:
# Inside: 10 5
# Outside: 10

# Q5.
count = 0
def increase():
    global count
    count += 1
increase()
print(count)
# Output:
# 1

# Q6.
def outer():
    print("Outer function")
    def inner():
        print("Inner function")
    inner()
outer()
# Output:
# Outer function
# Inner function

# Q7.
def add(a, b):
    return a + b
result = add(10, 5)
print("Result:", result)
# Output:
# Result: 15

# Q8.
def square(n):
    return n * n
def cube(n):
    return n * square(n)
print(cube(10))
# Output : 1000


# Q9.
def add(a, b):
    return a + b
def multiply_sum(x, y):
    return add(x, y) * 10
print(multiply_sum(5, 10))

# output : 150


# Q10.
def greet(name):
    return "Hello " + name
message = greet("Great Chinu")
print(message)
def display(msg):
    print("Message:", msg)
display(message)

# output : Hello Great Chinu
#          Message: Hello Great Chinu