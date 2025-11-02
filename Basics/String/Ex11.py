#remove vowels from string
S="authentic"
result=""
for char in S:
    if char not in "aeiouAEIOU":
        result+=char
print(result)
