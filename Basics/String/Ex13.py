#count of lettters,digits,spl characters
s="Hbin4@67"
lower_count=0
upper_count=0
digit_count=0
splChar_count=0
for ch in s:
    if ch.islower():
        lower_count+=1
    elif ch.isupper():
        upper_count+=1
    elif ch.isdigit():
        digit_count+=1
    else:
        splChar_count+=1
print("lower case:",lower_count)
print("Upper case:",upper_count)
print("Digits:",digit_count)
print("Special characters:",splChar_count)


        