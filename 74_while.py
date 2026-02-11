#  Write a program that takes a number as input and checks whether it is an 
# Armstrong number or not.
num=int(input("enter a num : "))#5
c=len(str(num))
sum=0
temp=num
while num>0:
    rem=num%10
    sum=sum+rem**c
    num=num//10
if sum==temp:
    print("num is armstrong")
else:
    print("num is not armstrog")    

