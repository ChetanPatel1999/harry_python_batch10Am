# Write a program to display all even numbers present in an list.
l1=[4,7,8,3,4,5,12] 

print("list all element are : ")
for num in l1:
    print(num,end=" ")

print("\nlist even element are : ")
for num in l1:
    if num%2==0:
        print(num,end=" ")    
