#wap to conut frequency of each caracter in given string. 
s="hello world in555stitute HELLO"
print("string : ",s)
for i in range(1,256):#
    c=0
    for ele in s:
        if ele.lower()==chr(i):
            c+=1
    if c>0 and chr(i)!=" ":
        print(f"{chr(i)} is appear {c} times" )
