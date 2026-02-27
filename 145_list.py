#  Write a program to check (search) given number is present or not present in array , using Linear 
# search.
l1=[34,65,2,78,65,89,54]
search=65
for num in l1:
    if num==search:
        print("num is find")
        break
else:
    print("num is not found")    