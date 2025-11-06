#Numbers divisible by 2 and 3 in set
num=set(range(1,22))
result={n for n in num if n%2==0 and n%3==0}
print(result)