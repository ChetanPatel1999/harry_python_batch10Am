#custome exception generate
num= int(input("enter a num : "))
try:
   if num<0:
     raise ValueError("nagative value error")
except ValueError as v:
   print(v) 
251_
else:
   print("your value : ",num)
print("program run succefully")

print("<---------------------------------->")

a=int(int(input("enter a  : ")))
b=int(int(input("enter b  : ")))
c=a+b
print("result : ",c)
print("program run succefully")