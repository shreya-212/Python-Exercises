# Check if a number is divisible by 5
n=int(input("Enter a number: "))
last_dig=n%10
if (last_dig==0 or last_dig==5):
    print(f"{n} is divisible by 5")
else:
    print(f"{n} is not divisible by 5")