# Write a program to count how many times each character appears in a string using 
# dictionary.
s="hello rydham why are you not come offline ?"
d1={}
for char in s :
    if char not in d1:   #d1={'h':1,'e':1,'l':2}
        d1[char]=1
    else:
        d1[char]=d1[char]+1

print(s)
# print(d1)

for key in d1:
    if key != " ":
        print(f"{key} is appear {d1[key]} tiems")