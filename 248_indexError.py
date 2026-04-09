#without exception handling
l1=[12,34,56,78]
print("welcome to my program")
index= int(input("enter a index : "))
try:
    print("value of given index : ",l1[index])
except:
    print("index error ...")    
print("program run succefully")

print("<---------------------------------->")

a=int(int(input("enter a  : ")))
b=int(int(input("enter b  : ")))
c=a+b
print("result : ",c)
print("program run succefully")