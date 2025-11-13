#Raise value exception
def check_num(num):
    if num<0:
        raise ValueError("Negative number not allowed")
    else:
        print("Number is valid")
try:
    num=int(input("Enter a number"))
    check_num(num)
 
except ValueError as e:
    print("Error: ",e)