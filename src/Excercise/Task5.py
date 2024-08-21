# Create a program that takes two numbers as input and prints whether the first number is greater than,
# less than, or equal to the second number.

num1 = float(input("Enter number 1:- "))
num2 = float(input("Enter number 2:- "))

if num1 > num2:
    print(num1, "is greater then", num2)
elif num1 < num2:
    print(num1, "is less then", num2)
else:
    print(num1, "equals", num2)
