#. Write a program to takes a number as input and calculates the sum of its 
# individual digits.
num=int(input("enter a num : "))#76243
res=0
while num:
    rem=num%10
    res+=rem
    num//=10
print(f"sum of individul digit = {res}")    