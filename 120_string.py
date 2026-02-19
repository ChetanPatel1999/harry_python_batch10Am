# Write a program to convert a string to uppercase.
s=input("enter a string : ")
newstr=''
for char in s:
    if char>='a' and char<='z':
        newstr=newstr+chr(ord(char)-32)
    else:
        newstr=newstr+char    
print("upperCase string : ",newstr)


