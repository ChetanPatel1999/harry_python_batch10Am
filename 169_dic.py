#  Write a program to swap keys and values of a dictionary.
d1={"pen":40,"color":30,"book":50}
d2={}

# for key in d1:
#     d2[d1[key]]=key

for key,value in d1.items():
    d2[value]=key

print(d1)
print(d2)