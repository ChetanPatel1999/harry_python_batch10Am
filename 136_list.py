# 82. Each sublist contains the individual digits of the corresponding number from the original list, excluding 
# all even digits. 
# Example: 
# Input list: [1352, 596, 467, 8932] 
# Output list: [[1, 3, 5], [5, 9], [7], [9, 3]]
l1=[1352, 596, 467, 8932] 
l2=[]
sub=[]
# for num in l1:
#     s=str(num)
#     for digit in s:
#         if int(digit)%2==1:
#             sub.append(int(digit))
#     l2.append(sub)
#     sub=[]        
# print("input list : ",l1)    
# print("output list: ",l2) 

for num in l1:
    while num>0:
        rem=num%10
        if rem%2==1:
            sub.append(rem)
        num=num//10
    l2.append(sub[::-1]) 
    sub=[]   
print("input list : ",l1)    
print("output list: ",l2)    

