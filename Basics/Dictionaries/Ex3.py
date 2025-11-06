#Adding items and print each key with its value
student={}
student["name"]="Sara"
student["age"]=22
student["course"]="Python"
print(student)

for key,value in student.items():
    print(key,":",value)