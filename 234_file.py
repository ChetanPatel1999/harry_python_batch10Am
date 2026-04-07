#how to write data  inside file
file = open(r"C:\Users\PC\Desktop\Demo\names.txt","a")
name=input("enter your name : ")
file.write(name+"\n")
file.close()

