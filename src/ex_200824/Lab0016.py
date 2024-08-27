# Grade Calculator

marks = float(input("Enter score you have achieved out of 100: "))

if marks >= 90.0 and marks <= 100.0:   # 90.0 <= marks <= 100.0  simplified chained comparison format
    print("You have scored grade A")
elif marks >= 80.0 and marks <= 89.9:
    print("You have secured Grade B")
elif marks >= 70.0 and marks <= 79.9:
    print("You have secured Grade C")
elif marks >= 60.0 and marks <= 69.9:
    print("You have secured Grade D")
elif marks > 100 or marks < 0:
    print("Please enter valid marked between 0 to 100 ")
else:
    print("Your grade is F")
