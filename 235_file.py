#how to write data  inside file
file = open(r"C:\Users\PC\Desktop\Demo\fruits.txt","w")
# l1=["apple\n","banana\n","mango\n","orange\n"]
l1=("apple\n","banana\n","mango\n","orange\n")
file.writelines(l1)
file.close()

