l1=[34,5,7,5,8,12,6,7,44,567,87,1,9]
s=44
find=False
for i in l1:
    if i==s:
        find=True
        break
if find:
    print("num is find")  
else:
    print("num is not find")       
    