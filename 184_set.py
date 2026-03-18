# Count number of vowels in a string using set. 
s="hello my name is chetan"
vovels=0
s1={"a","i","o","u","e"}
# for char in s:
#     if char.lower() in "aeiou":
#         vovels+=1

for char in s:
    if char.lower() in s1:
        vovels+=1
print(vovels)
