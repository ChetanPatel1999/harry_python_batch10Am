# 4. Write a program to make simple calculator. 
#       Press 1 to addition 
#       Press 2 to subtraction 
#       Press 3 to multiplication 
#       Press 4 to division 
num=int(input("""welcome to my calculator :
  Press 1 to addition 
  Press 2 to subtraction 
  Press 3 to multiplication 
  Press 4 to division 
  enter choise : """))
match num:
    case 1:
        print("you choosed addition app : ")
        a=int(input("enter frist num : "))
        b=int(input("enter second num : "))
        res=a+b
        print(f"{a} + {b} = {res}")
    case 2:
        print("you choosed subtraction app : ")
        a=int(input("enter frist num : "))
        b=int(input("enter second num : "))
        res=a-b
        print(f"{a} - {b} = {res}")
    case 3:
        print("you choosed multiplication app : ")
        a=int(input("enter frist num : "))
        b=int(input("enter second num : "))
        res=a*b
        print(f"{a} * {b} = {res}")  
    case 4:
        print("you choosed divide app : ")
        a=int(input("enter frist num : "))
        b=int(input("enter second num : "))
        res=a/b
        print(f"{a} / {b} = {res}")     
    case _:print("wrong number ! please enter 1 to 4")         