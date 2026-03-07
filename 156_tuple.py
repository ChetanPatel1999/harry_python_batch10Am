# count frequency of each element of tuple.
t1=(2,2,5,6,3,7,2,3,7)
l1=[]
for num in t1:
    if num not in l1:
      print(f"{num} = {t1.count(num)} times appear")
      l1.append(num)