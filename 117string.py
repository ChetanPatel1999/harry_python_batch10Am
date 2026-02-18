#Write a program  to separate individual characters from a string (like:- h e l l o  w o r l d  i n s t i t u t e). 
name="hello world institute"
for char in range(len(name)):
    if char!=len(name)-1 and name[char+1]!=' ' and name[char]!=' ':
       print(name[char],end="+")
    else:
       print(name[char],end=" ")   