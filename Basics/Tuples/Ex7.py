#print only string from mixed tuple
a=(1,"A",2,"B")
for i in a:
    if type(i)==str:
        print(i)
