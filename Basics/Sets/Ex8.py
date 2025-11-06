#Check if a word has all vowels
word="Beautification"
ch=set(word.lower())
vowels={'a','e','i','o','u'}
if vowels.issubset(ch):
    print("All vowels are present")
else:
    print("All vowels are present")