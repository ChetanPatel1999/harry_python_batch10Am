# Write a program to count the number of words in a string. 
s=input("enter a string : ")
c=0
for char in s:
    if char==' ':
        c+=1
print(f"total word : {c+1}")        
