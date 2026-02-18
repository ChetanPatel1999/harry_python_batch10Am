#pattern in py
for i in range(1,7):#1
    for s in range(i,6):
           print(" ",end="") 
    for j in range(1,i+1):
           if j==1 or i==4 or j==i:
                print("* ",end="")
           else:
                 print("  ",end="")            
    print()  