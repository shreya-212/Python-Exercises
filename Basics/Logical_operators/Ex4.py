#Digit to word form
num=int(input("Enter a single digit (0-9): "))
words=["zero","one","two","three","four","five","six","seven","eight","nine"]
if  0<=num<=9:
    print(words[num])
else:
    print("Invalid input")