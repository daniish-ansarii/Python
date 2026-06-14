# Question 1: Write a program that asks the user for their name and age, then prints a sentence like:
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"{name} is {age} years old.")

# Question 2: Take two numbers as input from the user and print their sum, difference, product, and quotient
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

sum = number1 + number2
difference = number1 - number2
product = number1 * number2
quotient = number1 / number2 if number2 != 0 else "undefined (division by zero)"

print(f"Sum: {sum}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")

# Question 3: Ask the user to enter two integers and one float. Convert them all to floats and print their average.
int1 = int(input("Enter the first integer: "))
int2 = int(input("Enter the second integer: "))
float1 = float(input("Enter a float: "))
average = ((int1) + (int2) + (float1)) / 3
print(f"The average is: {average}")                                 

# Question 4: The user enters a string containing a number (e.g., "42"). Convert it to an integer, a float, and a string.
number_str = input("Enter a number as a string: ")
number_int = int(number_str)
number_float = float(number_str)
print(number_str, type(number_str))
print(number_int, type(number_int))
print(number_float, type(number_float))
    
# Question 5: Evaluate the following expressions and print the results:
x = 10 + 3 * 2 ** 2
print(x)

# Question 6: Write a program to swap values of two numbers entered by the user.
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num1, num2 = num2, num1
print(f"After swapping: num1 = {num1}, num2 = {num2}")

# Question 7: Ask the user for temperature in Celsius and convert it to Fahrenheit. The formula is: F = C * 9/5 + 32
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius * 9/5 + 32
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

# Question 8: Take the radius of a circle as input from the user and calculate the area and circumference. The formulas are: Area = π * r^2 and Circumference = 2 * π * r (use 3.14 for π).
radius = float(input("Enter the radius of the circle: "))
pi = 3.14
area = pi * radius ** 2
circumference = 2 * pi * radius
print(f"Area of the circle: {area}")
print(f"Circumference of the circle: {circumference}")

# Question 9: Ask the user for: Principal amount, Rate of interest, and Time in years. Calculate the Simple Interest using the formula: SI = (P * R * T) / 100
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
simple_interest = (principal * rate * time) / 100
print(f"The Simple Interest is: {simple_interest}")

# Question 10: Take a decimal number as input (like 45.78) and print the integer part and the fractional part separately.
decimal_number = float(input("Enter a decimal number: "))
integer_part = int(decimal_number)
fractional_part = decimal_number - integer_part
print(f"Integer part: {integer_part}")
print(f"Fractional part: {fractional_part}")
