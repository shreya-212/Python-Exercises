#Local and global variable
n=10
def show():
    n=5
    print("Local variable:",n)
show()
print("Global variable:",n)