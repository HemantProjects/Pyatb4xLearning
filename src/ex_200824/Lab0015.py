# Find Max between three numbers

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
num3 = int(input("Enter Number 3: "))

if num1 > num2 and num1 > num3:
    print(f"num1 is the max {num1}")
elif num2 > num1 and num2 > num3:
    print(f"num2 is the max {num2}")
else:
    print(f"num3 is the max {num3}")

result = min(num1, num2, num3)  # to find min number in easy form
print("Minimum number is ", result)
