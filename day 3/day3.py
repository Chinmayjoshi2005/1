# Q1. Check whether a number is even or odd.
x = int(input("Enter the number : "))
if x % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# OR using ternary operator
x = int(input("Enter the number: "))
print("The number is even" if x % 2 == 0 else "The number is odd")

# Q2. Write a program to find the largest number among three numbers.
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))
if a >= b and a >= c:
    print("The largest number is : ", a)
elif b >= a and b >= c:
    print("The largest number is : ", b)
else:
    print("The largest number is : ", c)

# Q3. Write a program to check whether the year is a leap year or not.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Q4. Write a program that takes a percentage from the user and displays the grade according to the criteria.
percentage = float(input("Enter your percentage: "))
if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
elif percentage >= 40:
    grade = 'E'
else:
    grade = 'F'
print(f"Your grade is: {grade}")

# Q5. Write a program that checks if a given letter is a vowel (a, e, i, o, u) or a consonant.
letter = input("Enter a letter: ").lower()
if letter in 'aeiou':
    print(f"{letter} is a vowel.")
elif letter.isalpha() and len(letter) == 1:
    print(f"{letter} is a consonant.")
else:
    print("Please enter a valid single letter.")

# Q6. Write a basic calculator program that takes two numbers and an operator (+,-, *, /) as input and performs the specified operation.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
if operator == '+':
    print("Result:", num1 + num2)
elif operator == '-':
    print("Result:", num1 - num2)
elif operator == '*':
    print("Result:", num1 * num2)
elif operator == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")

# Q7. Write a program that takes a number as input and checks whether it is positive, negative, or zero.
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Q8. Write a program that checks if a username and password entered by the user match the pre-set values.
username = input("Enter username: ")
password = input("Enter password: ")
print("Choose an option:")
print("1. Login")
print("2. Exit")
print("3. Reset Password")
option = input("Enter your choice (1/2/3): ")
if option == '1':
    # Replace 'admin' and '1234' with desired credentials
    if username == "admin" and password == "1234":
        print("Login successful!")
    else:
        print("Invalid username or password.")
elif option == '2':
    print("Exiting program.")
elif option == '3':
    newpassword = input("Enter new password: ")
    password = newpassword
    print("Password has been reset.")
else:
    print("Invalid option.")

# Q9. Write a program that takes three sides of a triangle as input and checks if those sides form a valid triangle.
a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
c = float(input("Enter length of side c: "))
if (a + b > c) and (b + c > a) and (a + c > b):
    print("The sides form a valid triangle.")
else:
    print("The sides do not form a valid triangle.")

# Q10. Write a program that calculates the Body Mass Index (BMI) based on user input for weight (in kilograms) and height (in meters).
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obesity"
print("The category is:", category)

# Q11. Write a program that calculates the discount for a product based on its price.
price = float(input("Enter the price of the product: "))
if price > 1000:
    discount = 0.10 * price
elif 500 <= price <= 1000:
    discount = 0.05 * price
else:
    discount = 0
final_price = price - discount
print(f"The final price after discount is: {final_price:.2f}")

# Q12. Write a program that takes the name of a month as input and prints the number of days in that month. Consider leap years for February.
month = input("Enter the name of the month: ").strip().lower()
if month in ['january', 'march', 'may', 'july', 'august', 'october', 'december']:
    days = 31
elif month in ['april', 'june', 'september', 'november']:
    days = 30
elif month == 'february':
    year = int(input("Enter the year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days = 29
    else:
        days = 28
else:
    days = "Invalid month name"
print(f"The number of days in {month.capitalize()} is: {days}")

# Q13. Write a program that simulates a simple ATM.
print("Welcome to the ATM!")
balance = 1000.0  # Initial balance
print("Choose an option:")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
option = input("Enter your choice (1/2/3): ")
if option == '1':
    print(f"Your current balance is: ${balance:.2f}")
elif option == '2':
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        print(f"Previous balance is : ${balance:.2f}")
        balance += amount
        print(f"${amount:.2f} deposited. New balance is: ${balance:.2f}")
    else:
        print("Invalid deposit amount.")
elif option == '3':
    amount = float(input("Enter amount to withdraw: "))
    if 0 < amount <= balance:
        balance -= amount
        print(f"${amount:.2f} withdrawn. New balance is: ${balance:.2f}")
    else:
        print("Invalid withdrawal amount or insufficient balance.")
else:
    print("Invalid option.")

# Q14. Write a program that categorizes a given age into different groups.
age = int(input("Enter your age: "))
if 0 <= age <= 1:
    category = "Infant"
elif 2 <= age <= 4:
    category = "Toddler"
elif 5 <= age <= 12:
    category = "Child"
elif 13 <= age <= 19:
    category = "Teenager"
elif 20 <= age <= 59:
    category = "Adult"
elif age >= 60:
    category = "Senior"
else:
    category = "Invalid age"
print(f"You are categorized as: {category}")

# Q15. Write a program that takes an integer (1-7) as input and prints the corresponding day of the week.
day = int(input("Enter a number (1-7): "))
days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
print("The day is:", days.get(day, "Invalid input"))
