#finding mid character
s=input("Enter a string: ")
if len(s)%2==0:
    mid=len(s)//2
    result=s[mid-1:mid+1]
else:
    mid=len(s)//2
    result=s[mid]
print(result)