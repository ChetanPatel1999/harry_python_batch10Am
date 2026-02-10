#  Write a  program to find the 'Perfect' numbers within a given number of 
# ranges (using nested loop).

for num in range(1,100):
  sum=0
  for i in range(1,num):
    if num%i==0:
        sum+=i 
  if sum==num:
    print(num,end=" ")           
