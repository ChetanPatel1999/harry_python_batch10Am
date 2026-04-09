#without exception handling
l1=[23,56,78,89]
try:
    a=int(int(input("enter a  : ")))# hello
    b=int(int(input("enter b  : ")))# 0
    c=a/b
    print("result : ",c)
    index=int(int(input("enter index  : ")))# 0
    print("value of given index : ",l1[index])
    print("try run succefully")    
except ZeroDivisionError:
    c=a/2
    print("result : ",c) 
except ValueError:
    print("value error find") 
except IndexError:
    print("index error")
except :
    print("some thing wrong")                
print("program run succefully")

print("<---------------------------------->")

a=int(int(input("enter a  : ")))
b=int(int(input("enter b  : ")))
c=a+b
print("result : ",c)
print("program run succefully")