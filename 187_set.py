# Count frequency of elements using set + list in list element. 
l1=[3,4,2,3,4,5,6,3,4,5]

# l2=[]
# print(l1)
# for num in l1:
#     if num not in l2:
#        print(f"{num} is appear {l1.count(num)}")
#        l2.append(num)

# s1=set(l1)
# print(l1)
# for num in s1:
#     print(f"{num} is appear {l1.count(num)}")

d1={}
for num in l1:
    if num not in d1:
        d1[num]=1
    else:
        d1[num]+=1
print(l1)        
print(d1)        

