#  Write a program to find the maximum element in an array. 
l1=[45,63,7,89,4,6,9]
# max=float('-inf') # its proivide minimum value in python
# max=float('inf') #its proivide maximum value which store in python
max=l1[0]
for num in l1:
    if max<num:
        max=num # 5
print("list : ",l1 , "\nmax value = " , max)        
