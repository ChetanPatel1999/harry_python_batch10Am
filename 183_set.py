# Remove duplicate elements from a list using set.
l1=[2,4,3,5,3,5,2,2]
print(l1)
l2=[]

for i in range(len(l1)):# i=2
    for j in range(i+1,len(l1)):# j= 2
        if l1[i]==l1[j]:
            break
    else: 
        l2.append(l1[i])  

# for i in l1:
#     if i not in l2:
#         l2.append(i)

# s1=set(l1)
# l1=list(s1)
print(l1)
print(l2)