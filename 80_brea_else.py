#  Write a program that takes a number and a single digit as input, and checks 
# whether the digit exists in the given number or not. 
num=64723
digit=5
while num>0:
    rem=num%10
    if rem==digit:
        print("digit is find")
        break
    num=num//10  
else:
    print("digit is not find")
