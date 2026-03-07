#write a program to find index of given element
t1=(2,2,5,6,3,7,2,3,7)
num=77
for i in range(len(t1)):
    if num==t1[i]:
        print(f"index = {i}")
        break
else:
    print("element not find")    
