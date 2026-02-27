#   Write a program to check (search) given number is present or not present in array , using binary 
# search.
l1=[34,65,2,78,89,54,7,12,8,3,4,9]
l1.sort()
print(l1)
search=4
f=0
l=len(l1)-1 #11
print(l)
#[2, 3, 4, 7, 8,    9   , 12, 34,  54 , 65,   78  , 89]
while f<=l: #9<9
    m=(f+l)//2 #9
    print(m)
    if l1[m]==search:
        print("num is find")
        break
    elif l1[m]<search:
        f=m+1  #9
    else:
        l=m-1  # 9
else:
    print("num is not found")           

   
