# Write a program to find the sum of all elements in an array.
n=int(input("enter list length : "))#5
l1=[]
for i in range(n):
    element=int(input(f"enter list element{i+1} : "))
    l1.append(element)

sum=0
for num in l1:
    sum+=num
print("list  = ",l1)    
print("list element sum = ",sum)    
print("list element average = ",sum/n)    