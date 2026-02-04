#Calculate power of a number without using pow() and exponent operator.
num=int(input("enter a num : "))#5
p=int(input("enter power : "))#4
i=1
res=1
while i<=p:
    res=res*num
    i+=1
print(f"result for {num} which power is {p} = {res}")    

