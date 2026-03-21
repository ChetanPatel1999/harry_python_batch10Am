lst = [1, 2, 3, 3, 5, 6, 7, 8]

for x in lst[:]:   # copy of list
    print(x)
    if x % 2 != 0:
        lst.remove(x)

print(lst)