#Check if a list has duplicates
num=[1,2,3,4,2]
uniq=set(num)

if len(num)!=len(uniq):
    print("List has duplicates")
else:
    print("No duplicates")
      