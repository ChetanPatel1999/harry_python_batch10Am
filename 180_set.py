# Convert string into set and display unique characters.

str1="ababcdfcd"
newstr="" # abcdf
# for char in str:
#     if char not in newstr:
#         newstr+=char
s1=set(str1)
for char in s1:
     newstr+=char
print(str1)
print(newstr)
