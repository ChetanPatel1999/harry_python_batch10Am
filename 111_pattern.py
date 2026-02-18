#pattern in py
for i in range(1,6):#1
    for s in range(i,5):
           print(" ",end="") 
    for j in range(1,i+1):
           if j==1 or i==5 or j==i:
                print("* ",end="")
           else:
                 print("  ",end="")            
    print()  