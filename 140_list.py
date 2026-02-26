#  Write a  program that accepts some integers from the user and finds the highest value and the input 
# position.
l1=[12,4,3,78,5,99,2]
max=l1[0]
pos=0
# for i in range(len(l1)):
#     if max<l1[i]:
#         max=l1[i]
#         pos=i
# print("list : ",l1 , "\nmax value = " , max)  
# print("element position  : ",pos+1)

for i,num in enumerate(l1):
    if max<num:
        max=num
        pos=i
print("list : ",l1 , "\nmax value = " , max)  
print("element position  : ",pos+1)