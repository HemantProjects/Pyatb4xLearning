# Match statement
browser_name = input("Enter the name of the Browser:- ")
browser_name = browser_name.lower()    # To change it to lower case
match browser_name:
    case "chrome":
        print("Execute Chrome browser")
    case "firefox":
        print("Execute Firefox browser")
    case "Safari":
        print("Execute Safari browser")
    case "edge":
        print("Execute Edge browser")
    case _:
        print("Invalid browser entered")
