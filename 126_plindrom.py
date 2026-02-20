# Write a program to check whether a string is a palindrome or not.
#  naman  malayalam  madam  dad mom 
s=input("enter string : ")
# if s==s[::-1]:
#     print("string is plindrom")
# else:
#     print("string is not plindrom") 
# 

# rev=""
# for i in range(len(s)-1 ,-1,-1):
#     rev+=s[i]
# if s==rev:
#     print("string is plindorm")
# else:
#     print("styring is not plindrom")    
# 


# rev=""
# #hello
# for i in s:
#     rev=i+rev  # olleh
# if s==rev:
#     print("string is plindorm")
# else:
#     print("string is not plindrom")     


i,j=0,len(s)-1
while i<j:
    if s[i]!=s[j]:
        print("not plindrom")
        break
    i+=1
    j-=1
else:
    print("string is plindrom")    