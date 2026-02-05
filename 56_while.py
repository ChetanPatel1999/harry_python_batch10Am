# Write a program that takes a number as input and displays its digits in 
# reverse order as a new number.
num=int(input("enter a num : "))#6758
# rev=0
# while num:
#     rem=num%10
#     rev=rev*10+rem #576
#     num//=10
# print("reverse number = %d"%rev)    
print(f"reverse number = {int(str(num)[::-1])}")    