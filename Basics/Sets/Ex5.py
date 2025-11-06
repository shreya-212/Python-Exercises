#Add vowels of a word to a set
word="authentic"
vowel=set()
for ch in word:
    if ch in "aieouAEIOU":
        vowel.add(ch)
print(vowel)
