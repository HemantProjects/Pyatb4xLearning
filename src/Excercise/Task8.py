# Triangle Classifier

L1 = int(input("Enter length 1 of the triangle: "))
L2 = int(input("Enter length 2 of the triangle: "))
L3 = int(input("Enter length 3 of the triangle: "))

if L1 == L2 == L3:
    print("Triangle is Equilateral")
elif L1 == L2 or L1 == L3 or L2 == L3:
    print("Triangle is of type Isosceles")
else:
    print("Triangle is of type Scalene")
