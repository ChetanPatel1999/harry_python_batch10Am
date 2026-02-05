#. Write a program that takes a number and a single digit as input, and checks 
# whether the digit exists in the given number or not.
num=int(input("enter a num : "))#76243
d=int(input("enter a digit : "))#2
isFind=False
#count=0
while num:#76243
    rem=num%10
    if rem==d:
        isFind=True
        #count+=1
    num//=10
if isFind: #count>0
    print("num is exist")# count value 
else:
    print("num is not exist")


 