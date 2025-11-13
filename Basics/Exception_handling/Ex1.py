#Division be zero
try:
    a=int(input("Enter a number:"))
    b=int(input("Enter a number:"))
    result=a/b
    print("Result:",result)
except ZeroDivisionError:
    print("Error:Division by zero")
