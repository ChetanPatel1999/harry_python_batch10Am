#  Write a to find the HCF (Highest Common Factor) of two numbers. 
n1=30
n2=12
min= n1 if n1<n2 else n2
while True:
    if n1%min==0 and n2%min==0:
        print(f"HCF = {min}")
        break
    min-=1

