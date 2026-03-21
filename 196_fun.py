def evenElementUpdate(lst):
    i=0
    while i< len(lst): #
        if lst[i]%2!=0:
            lst.remove(lst[i])
            i-=1
        i+=1    
    
def evenElement(lst):
    nlst=lst.copy()
    i=0
    while i< len(nlst): #
        if nlst[i]%2!=0:
            nlst.remove(nlst[i])
            i-=1
        i+=1   
    return nlst          

def mylist(lst):
    lst=[num for num in lst if num%2==0]
    return lst

l1=[2,5,3,6,7,8]
print(l1)
# newlist=evenElement(l1)
# evenElementUpdate(l1)
mylist(l1)
print(l1)
# print(newlist)