#Count of vowels in a string
S="authentic"
count=0
for char in S:
    if char in "aeiouAEIOU":
        print(char)
        count+=1
print("Count of vowels: ",count)
