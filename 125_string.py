#wap to print sum 1 to n
n=15
sum=0
res=""
for i in range(1,n+1):
    res+=str(i)+"+"
    sum+=i
print(res[:len(res)-1],"=",sum)    


