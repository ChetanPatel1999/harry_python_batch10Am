# Write a program to interchange first and last elements in an array. 
l1=[12,45,67,89,33]
print("before interchange : ",l1)
# temp=l1[0]
# l1[0]=l1[len(l1)-1]
# l1[len(l1)-1]=temp

temp=l1[0]
l1[0]=l1[-1]
l1[-1]=temp
print("after interchange : ",l1)