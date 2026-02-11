#  Write a to find the LCM (Lowest common multiple) of two numbers. 
n1=25
n2=50
max= max(n1,n2)
while True:
    if max%n1==0 and max%n2==0:
        print(f"LCM = {max}")
        break
    max+=25

