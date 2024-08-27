# Take age from user and check if he/she is allowed for Driving license

age = int(input("Enter Your age:- "))

if age >= 18:
    print(f"Congrats, You are allowed to go for driving license.You are {age} old")
else:
    print(f"Sorry, you are not allowed for driving license. You are {age} old")
