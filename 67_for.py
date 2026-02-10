# 6. Write a program to find the sum of the series [1 +11 + 111 + 1111 + .. n ] 
# terms.
n=int(input("enter how many element you want this series : "))
ele=1
sum=0
for i in range(1,n+1):
    if i!=n:
     print(ele,end=" + ")
    else:
      print(ele,end=" ")   
    sum+=ele
    ele=ele+10**i
print("= ",sum)    
