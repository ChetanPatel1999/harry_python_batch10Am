def add():
    print("this is addition function :")
    a=int(input("enter a : "))
    b=int(input("enter b : "))
    c=a+b
    print(f"addition of {a} and {b} = {c}")

def sub():
    print("this is subtraction function :")
    a=int(input("enter a : "))
    b=int(input("enter b : "))
    c=a-b
    print(f"subtraction of {a} and {b} = {c}")  

def multiplication():
    print("this is  multiplication function :")
    a=int(input("enter a : "))
    b=int(input("enter b : "))
    c=a*b
    print(f" multiplication of {a} and {b} = {c}")

def division():
    print("this is  division function :")
    a=int(input("enter a : "))
    b=int(input("enter b : "))
    if b!=0:
       c=a/b
       print(f" division of {a} and {b} = {c}")
    else:
       print("not divide by 0")    

# print("hello welcome to my program")    
# add()  #function calling
# add()
# sub()

# for i in range(5):# i = 1
#     add()

while True:
    num=int(input("""welcome to my calculator :
    Press 1 to addition 
    Press 2 to subtraction 
    Press 3 to multiplication 
    Press 4 to division 
    enter choise : """))
    match num:
        case 1:
            add()
        case 2:
            sub()
        case 3:
            multiplication() 
        case 4:
            division()    
        case _:print("wrong number ! please enter 1 to 4")         
    if (int(input("press 1 to continiue : "))) != 1:
        break
