 # Here Topics is Conditional Statements, Loops, Functions

 # Conditional Statements
age = 15

if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult.")
else:
    print("You are an adult.") 


color = input("Enter a color: ")

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Caution")
elif color == "green":
    print("Go")
else:
    print("Invalid color") 


username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "password123":
    print("Access granted.")
else:
    print("Access denied.") 

# nested if statements
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "password123":
    print("Access granted.")
else:
    if username != "admin":
        print("Invalid username.")
    else:
        print("Invalid password.")  

#Match case statements
day = input("Enter a day of the week: ")

match day:
    case "Monday":
        print("Start of the work week.")
    case "Wednesday":
        print("Midweek day.")
    case "Friday":
        print("End of the work week.")
    case _:
        print("Invalid day.")

#  --- * Loops * ---
#  --- * while loop * ---
#we use while loop to execute a block of code repeatedly as long as a condition is true

counter = 0
while counter < 5:
    print("Hello, World!")
    counter += 1

# practice question: print the first 10 natural numbers using a while loop
counter = 1
while counter <= 10:
    print(counter)
    counter += 1

# practice question: print the first 10 natural numbers in reverse order using a while loop
i = 10
while i >= 1:
    print(i)
    i -= 1

# practice question: print multiplication table of a number entered by the user using a while loop
number = int(input("Enter a number to see its multiplication table: "))
counter = 1
while counter <= 10:
    print(f"{number} x {counter} = {number * counter}")
    counter += 1

# break and continue statements
counter = 0
while counter < 10:
    counter += 1
    if counter == 5:
        break  # Exit the loop when counter is 5  
    print(counter)

counter = 0
while counter < 10:
    counter += 1
    if counter == 5:
        continue  # Skip the rest of the loop when counter is 5  
    print(counter)

# practice question: print all the even numbers from 1 to 10 using a while loop and continue statement
i = 0
while i <= 10:
    i += 1
    if i % 2 != 0:
        continue  # Skip odd numbers
    print(i)

# practice question: print all the odd numbers from 1 to 10 using a while loop and continue statement
i = 0
while i <= 10:
    i += 1
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)

# --- * for loop * ---
# we use for loop sequential traversal of a sequence (like list, tuple, string) or range of numbers

string = "Hello"
for var in string:
    print(var)

# here in is membership operator which checks if a value is present in a sequence (like list, tuple, string) or not

if 'e' in string:
    print("e is present in the string")

# practice question: print the first 10 natural numbers using a for loop start from 1
for i in range(1, 11):
    print(i)

# practice question: count the number of occurrences of 'i' in the word "artificial intelligence"
word = "artificial intelligence"
counter = 0
for ch in word:
    if ch == 'i':
         counter += 1
print("Number of occurrences of 'i':", counter)

# practice question: Print vowels in the word "artificial intelligence"
word = "artificial intelligence"
counter = 0
for ch in word:
    if ch in 'aeiou':
        counter += 1
print("Number of vowels:", counter)

# range function --> it generates a sequence of numbers based on the specified start, stop, and step values
# range(5) --> 0, 1, 2, 3, 4
# range(1, 6) --> 1, 2, 3, 4, 5
# range(0, 10, 2) --> 0, 2, 4, 6, 8

# practice question: print the first 10 even numbers using a for loop and range function
for i in range(0, 20, 2):
    print(i)

# practice question: print the sum of first 'n natural numbers.
n = int(input("Enter a number: "))
total_sum = 0
for i in range(1, n+1):
    total_sum += i
print(f"The sum of the first {n} natural numbers is: {total_sum}")

# Functions
# A function is a reusable block of code that performs a specific task. It can take inputs (parameters) and can return a value. 
# Functions help in breaking down a program into smaller, modular pieces, making it easier to read, maintain, and debug.

def hello():
    print("Hello, World!")

hello()  # Calling the function to execute its code

#practice question: Write a function that takes two numbers as input and returns their sum.

def sum_numbers(a, b):
    sum = a + b
    return sum

result = sum_numbers(5, 10)  # Calling the function with arguments 5 and 10
print(f"The sum of 5 and 10 is: {result}")

# practice question: Write a function that takes a string as input and returns the number of vowels in that string.
def count_vowels(s):
    count = 0 
    for ch in s:
        if ch in 'aeiou':
            count += 1
    return count   

result = count_vowels(input("Enter a string: "))  # Calling the function with user input
print(f"The number of vowels in the string is: {result}")   

# practice question: function that takes three numbers as input and returns the average of those numbers.
def average_of_three(a, b, c):
    average = (a + b + c) / 3
    return average

print(average_of_three(10, 20, 30))  # Calling the function with arguments 10, 20, and 30

# Type of functions:
# 1. Built-in functions: These are functions that are provided by the programming language itself
# 2. User-defined functions: These are functions that are defined by the user to perform specific tasks

# -- > Built-in functions examples:
# print() - used to display output to the console
# range() - used to generate a sequence of numbers  
# input() - used to take input from the user
# type() - used to get the data type of a variable
# int() - used to convert a value to an integer

# -- > User-defined functions examples: -- > created by the user to perform specific tasks
# def greet(name):
#     print(f"Hello, {name}!")  

# 3. Lambda functions: These are anonymous functions that can have any number of arguments but only one expression. 
#    They are often used for short, simple functions that are not reused elsewhere in the code.

add = lambda x, y: x + y  # A lambda function to add two numbers
print(add(5, 10))  # Calling the lambda function with arguments 5 and 10

# practice question: Write a function to print the factorial of n
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Calling the function with argument 5

#another way to calculate factorial using a for loop
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
