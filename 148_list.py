# List Comprehension  
 
# List comprehension offers a shorter syntax when you want to create a new list based 
# on the values of an existing list.  

# l1=[4,6,5,7,8,9]
# l2=[]
# for num in l1:
#     square=num*num
#     l2.append(square)
# print(l1)    
# print(l2)   

#above same work  using list comprehension
# l1=[4,6,5,7,8,9]
# l2=[num+5 for num in l1]
# print(l1)    
# print(l2)   

#make a new list only containe even element
# l1=[4,3,7,6,5,2]
# l2=[]
# for num in l1:
#     if num%2==0:
#         l2.append(num)
# print(l1)
# print(l2) 
# 
# same proble usiing list comprehension
# l1=[4,3,7,6,5,2]
# l2=[num for num in l1 if num%2==0]
# l3=[num for num in l1 if num%2==1]
# print(l1)
# print(l2)       
# print(l3)   

# make a new list which contain only greter then 5 and less then 10 elements
# l1=[44,59,3,7,6,5,2,9,12,56,]
# # l2=[num for num in l1 if num>5]
# l2=[num for num in l1 if num>5 and num<10]
# print(l1)
# print(l2)    
#
 
#new list contain only element which containg 3 digit in element
l1=[345,678,98,66,34,23,456]
l2=[num for num in l1 if '3' in str(num)]  
print(l1)
print(l2)

      