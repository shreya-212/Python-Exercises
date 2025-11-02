#remove character at odd indices
s="abcd"
new=""
for i in range(len(s)):
    if i%2==0:
        new+=s[i]
print(new)
        

