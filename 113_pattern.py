#pattern in py
for i in range(1,6):#1
    for j in range(1,6):
       if i==1 or i==5 or j==1 or j==5:
           print("* ",end="") 
       else:
           print("  ",end="")       
    print()  
for i in range(1,6):#2
    for j in range(1,6):
       if i==j and i!=1  or j==1 and i!=1:
           print("* ",end="") 
       elif i==1:
          print("",end="")       
       else:
           print("  ",end="") 
    if i==1:
        continue              
    print()     