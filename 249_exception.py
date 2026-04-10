try:
    a=int(int(input("enter a  : ")))# 
    b=int(int(input("enter b  : ")))# 
    c=a/b 
except ZeroDivisionError as z:
    print(z)   
else:
    print("result : ",c)     # safe satament write in else block
finally:
    print("its run always")                        
print("program run succefully")

print("<---------------------------------->")

a=int(int(input("enter a  : ")))
b=int(int(input("enter b  : ")))
c=a+b
print("result : ",c)
print("program run succefully")