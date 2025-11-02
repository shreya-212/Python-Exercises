#find non repeating character
s="aabbcd"
for ch in s:
    if s.count(ch)==1:
         print(ch)
         break

else:
    print("No repeating character")