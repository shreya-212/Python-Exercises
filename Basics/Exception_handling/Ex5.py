#File not found error
try:
    file=open("Data.txt","r")
    content=file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found")
finally:
    print("Execution complete")