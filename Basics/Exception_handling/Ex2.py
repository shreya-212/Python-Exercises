#Value error
try:
    a=int(input("Enter a number:"))
    b=int(input("Enter a number:"))
    result=a/b
    print("Result:",result)

except ValueError:
    print("Error: Enter only number")
except ZeroDivisionError:
    print("Error:Division by zero")
