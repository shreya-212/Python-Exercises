#Function to check if a word is a palindrome
def palindrome(word):
    word=word.lower()
    return word==word[::-1]

result=palindrome("madam")
if result==True:
    print("Is a palindrome")
else:
    print("Is not a palindrome")