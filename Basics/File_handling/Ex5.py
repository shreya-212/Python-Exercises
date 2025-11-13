#using with open
with open("notes.txt","r") as f:
    content=f.read()
    words=content.split()
    print("Count of words:",len(words))
    