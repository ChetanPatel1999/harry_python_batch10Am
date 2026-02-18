#pattern in py
for i in range(70,64,-1):#1
    for j in range(65,i+1):
        if j!=70:
            print(chr(j),end=" ") 
    for s in range(70,i*2-69,-1):
        print("  ",end="")        
    for k in range(i,64,-1):
        print(chr(k),end=" ")        
    print()  
    