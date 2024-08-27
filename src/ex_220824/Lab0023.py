user_type = input("Enter User type from 'admin', 'manager','operator','guest':- ")
user_type = user_type.lower()
match user_type:
    case "admin" | "manager":
        print("Hello, sir")
    case "operator":
        print("Hello, operator")
    case "guest":
        print("Hello, Guest")
    case _:
        print("Hello, There")
