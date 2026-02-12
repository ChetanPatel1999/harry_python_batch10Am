# Write a program to check given number is prime or not. 
num=int(input("enter a num : "))#444
i=1
factorsCount=0
while i<=num:
    if num % i == 0:
      factorsCount+=1 # 3
    if factorsCount>2:
       break  
    i+=1
if factorsCount==2:
   print("prime number") 
else:
   print("not prime number")     

