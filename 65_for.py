#  Calculate power of a number without using pow().
num=int(input("enter a num : "))#5
p=int(input("enter a pow : "))#3
res=1
for i in range(p):
    res=res*num
print(f"res = {res}")    

