#wap to conut frequency of each caracter in given string. 
s="hello world in555stitute"
l1=[]
print("string : ",s)
for char in s: # l
    c=0
    if char not in l1 and char !=" ":#['h','e','l']
      for ele in s:
        if char==ele:
           c+=1       
    if c>0:
       print(f"{char} is apper {c} times")
       l1.append(char)
