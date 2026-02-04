# Wap to find greatest number among has given three numbers without 
# using (&&)  logical and operator. 
a=int(input("enter a : "))
b=int(input("enter b : "))
c=int(input("enter c : "))
if a>b:
    if a>c:
        print(f"greatest num : {a}")
    else:
        print(f"greatest num : {c}")    
else:
    if b>c:
        print(f"greatest num : {b}")   
    else:
        print(f"greatest num : {c}")         