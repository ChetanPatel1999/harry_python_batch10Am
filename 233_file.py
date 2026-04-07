#how to write data  inside file
file = open(r"C:\Users\PC\Desktop\Demo\cube.txt","a")
num=int(input("enter a num : "))
cube=num*num*num
print(f"cube of {num} = {cube}")
file.write(f"cube of {num} = {cube}\n")
file.close()

