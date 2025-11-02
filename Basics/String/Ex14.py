#find largest word in sentence
s="this is a string"
largest=""
words=s.split()
for word in words:
    if len(word)>len(largest):
        largest=word
print("Largest word: ",largest)