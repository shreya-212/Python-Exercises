#Find average of each student
student={"A":[80,90,100],"B":[70,60,90]}
for name,marks in student.items():
    avg=sum(marks)/len(marks)
    print(name,"average: ",avg) 