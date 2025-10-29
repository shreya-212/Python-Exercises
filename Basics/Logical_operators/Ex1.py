#Take a character and check if its a letter , a digit or neither
ch=input("Enter a character: ")
if ch.isalpha():
    print("It is a letter")
elif ch.isnumeric():
    print("It is a digit")
else:
    print("It is neither a letter nor a digit")