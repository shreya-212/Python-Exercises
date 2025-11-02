#remove duplicate characters from word
s="wordssss"
result=""
for ch in s:
    if ch not in result:
        result+=ch
print(result)