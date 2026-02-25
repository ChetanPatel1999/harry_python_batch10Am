# . Write a program to display the list elements in reverse order.
l1=[12,34,56,78,90]
print("list element are : ")
for num in l1:
    print(num,end=" ")

print("\nreverse list element : ") 
for i in range(len(l1)-1,-1,-1):
    print(l1[i],end=" ")


# l2=l1[ : :-1]
# print("\nreverse list element : ")    
# for num in l2:
#     print(num,end=" ")