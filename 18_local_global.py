#local and global variable in python
age=45   #global variable
def add():
    x=12 #local variable
    y=5  #local variable
    z=x+y
    print("addition : ",z)
    print("age : ",age)

def sub():
    a=12 #local variable
    b=5  #local variable
    c=a-b
    print("addition : ",c)
    print("age : ",age)

def getAge():
    global age
    print("age in function : ",age)
    age=89
    print("age in function : ",age)


getAge()
print("age : ",age)




