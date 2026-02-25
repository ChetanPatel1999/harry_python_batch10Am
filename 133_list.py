# Write a program to count how many even numbers are present in an list.
l1=[4,7,8,3,4,5,12,7,16] 

print("list all element are : ")
for num in l1:
    print(num,end=" ")

count=0
for num in l1:
    if num%2==0:
        count+=1 
print("\nall even element count = ",count)        