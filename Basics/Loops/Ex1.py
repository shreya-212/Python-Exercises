#Sum of digits of  numbers
num=int(input("Enter a number: "))
tot=0
while num>0:
    tot+=num%10
    num//=10
print("Sum of digits: ",tot)
