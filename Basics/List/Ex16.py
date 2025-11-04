#Find difference between largest and smallest number
l=[10,3,8,5]
largest=l[0]
smallest=l[0]
for i in l:
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i
diff=largest-smallest
print(diff)
