file = open(r"C:\Users\PC\Desktop\Demo\fruits.txt","r")
# data = file.read(5)
# data = file.readline()
# print(data)
# data = file.readline()
# print(data)
data = file.readlines()   # return a list of line

print(data)

for line in data:
    print(line) 
file.close()