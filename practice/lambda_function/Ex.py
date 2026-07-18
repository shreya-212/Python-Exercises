# A lambda function is a small anonymous function used for simple,one-line operations.



square=lambda x: x*x
print(square(5))


add=lambda a,b: a+b
print(add(10,45))


is_even=lambda n:n%2==0
print(is_even(20))


maximum_check=lambda a,b:a if a>b else b
print(maximum_check(30,50))


last_char = lambda s: s[-1]
print(last_char([1,2,3,4]))