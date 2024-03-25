def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"


print("___________________")
print("|                 |")
print("|   CALCULATOR    |")
print("|                 |")
print("|                 |")
print("___________________")

while True:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("_______________________")
    print("     + For Addition    ")
    print("   - For Subtraction   ")
    print("     / For Division    ")
    print(" *  For Multiplication ")
    print("_______________________")
    o=input("Choose one from options:")

    if (o=='+'):
        print(add(a,b))
    elif(o=="-"):
        print((subtract(a,b)))
    elif(o=="/"):
        print("divide (a,b)")
    elif(o=='*'):
        print(multiply(a,b))
    else:
        print("Error!!!! Wrong inputtt")


    

    
    

