#Take a list of names and print all names that start with a vowel
names=["Eva","Ana","Sara","Ria"]
vowels="aeiou"
for i in names:
    if i[0].lower() in vowels:
        print(i)

    