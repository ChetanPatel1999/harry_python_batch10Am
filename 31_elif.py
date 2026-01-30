#  Write a program to find greatest number among has given three numbers.
a=int(input("enter a :"))
b=int(input("enter b :"))
c=int(input("enter c :"))
if a>b and a>c:
    print(f"greatest num : {a}")
elif b>c:
    print(f"greatest num : {b}")
else:
    print(f"greatest num : {c}")    
