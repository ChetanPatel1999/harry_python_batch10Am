# Write a program to input and print all elements of an list.
n=int(input("enter list length : "))#5
l1=[]
for i in range(n):
    element=int(input(f"enter list element{i+1} : "))
    l1.append(element)

print("list values : ",l1)

print("list element in differen line : ")
for num in l1:
    print(num)


    