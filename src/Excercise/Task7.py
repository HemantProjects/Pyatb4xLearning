# Check Leap Year

year = int(input("Enter a Year to check if the year is Leap Year:- "))

if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print(f"Entered year: {year} is a leap year")
else:
    print(f"Entered year {year} is not a leap year")