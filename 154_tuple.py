t1=(12,34,56,78)
print(t1)
l1=list(t1)  # conver tuple in list
l1.append(500)   # change in list
t1=tuple(l1)  # convert list in again tuple
print(t1)