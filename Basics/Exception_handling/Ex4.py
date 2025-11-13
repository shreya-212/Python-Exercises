#Try-except-else-finally
try:
    num=int(input("Enter a number:"))
    print("Num:",num)
except ValueError:
    print("Error:Enter a number")
else:
    print("No errors occured")
finally:
    print("Execution finish ")