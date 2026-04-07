# how to read file in python

file = open(r"C:\Users\PC\Desktop\Demo\fruits.txt","r")
data = file.read()

print(data)

l1=data.split()

print(l1)

c=0
for word in l1:
    if word=="fruit":
        c+=1

print("fruit word is apper in file = ",c)

c=0
for char in data:
    print(char)
    c+=1

print("total char in file : ",c)
file.close()
