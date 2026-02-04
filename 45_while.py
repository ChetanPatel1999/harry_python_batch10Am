#wap to print 1 to n even numbers
n=int(input("enter a num : "))#10
i=1
print("even number : ",end="")
while i<=n:
    if i%2==0:
        print(i,end=" ")
    i+=1 #3  
print("\nodd number : ",end="")
i=1
while i<=n:
    if i%2==1:
        print(i,end=" ")
    i+=1 #3 
