#Check if a number is a leap year
year=int(input("Enter a number: "))
if (year%400==0) or (year%4==0 and year%100!=0):
    print(" Leap year")
else:
    print("Not a leap year")