#Element common in atleast two sets
a={1,2,3,4}
b={3,4,5,6}
c={4,5,6,7}
result=(a&b)|(b&c)|(a&c)
print("Element common in at least two sets: ",result)