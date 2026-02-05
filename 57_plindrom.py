# . Write a program that takes a number as input and checks whether it is a 
# palindrome or not. (A number is a palindrome if it reads the same forward 
# and backward.).
num=int(input("enter a num : "))#454
# temp=num
# rev=0
# while num:
#     rem=num%10
#     rev=rev*10+rem #454
#     num//=10
# if rev==temp:
#     print("num is plindrom")
# else:
#     print("num is not plindorm")       
rev=int(str(num)[::-1])
if num==rev:
    print("plindrom")
else:
    print("not plindrom")    