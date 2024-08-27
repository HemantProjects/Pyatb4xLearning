# Find Maximum between two numbers.

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

if num1 > num2:
    print(f"Num1 is Max and number is {num1}")
elif num2 > num1:
    print(f"Num 2 is Max and number is {num2}")
else:
    print("Both numbers are same")

print(max(num1, num2))               # Easy way to find Max number if not wanna go with loop
