#   Write a program to reverse each word in a string without changing their order. 
#hello my name is chetan
#olleh ym eman si natehc
s=input("enter string : ")
list1=s.split()
newstr=''
for ele in list1:
    newstr=newstr+ele[::-1]+" "
print("reverse word ",newstr)    