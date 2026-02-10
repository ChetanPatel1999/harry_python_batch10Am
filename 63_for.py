#wap to print 1 to 10 even numbers
n=int(input("enter a num : "))#10
for i in range(1,n+1):
    if i%2==0:
        print(i,end=" ")