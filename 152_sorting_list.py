#wap to sort list element in assending order using selection sort.
l1=[5,12,3,8,6]
print(l1)
#[3,5,12,8,6]
for i in range(len(l1)-1): #(0,1   ,2,3,4)
    min=l1[i] #12
    index=i  #1
    for j in range(i+1,len(l1)): # (2,3  ,4 )
        if min>l1[j]:
            min=l1[j]  #5
            index=j #2
    temp=l1[i]
    l1[i]=l1[index]
    l1[index]=temp

print(l1)