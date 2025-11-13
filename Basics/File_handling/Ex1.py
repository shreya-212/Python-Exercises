#Reading from a file
f=open("notes.txt","r")
content=f.read()
print(content)
f.close()