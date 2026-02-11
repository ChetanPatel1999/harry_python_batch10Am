#  Write a program to convert a decimal number into binary without using an 
# array. 
decimal=int(input("enter a num : "))
binary=""
while decimal>0:
    rem=decimal%2
    binary=str(rem)+binary #1100
    decimal=decimal//2
print("binary num = ",binary)    