#  Write a program to convert a binary number into a decimal number 
# without using array, function and while loop.
binary=int(input("enter a num : "))#1111
decimal=0
base=1
while binary>0:#1
    rem=binary%10  # 1
    decimal=decimal+rem*base #15
    base=base*2  #16
    binary=binary//10 # 0
print(f"decimal = {decimal}")    