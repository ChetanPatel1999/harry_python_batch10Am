#difference()
# return only differnet element from another set
s1={12,9,5,7,8}
s2={7,8,25,30,22}
# s3=s2.difference(s1)
# s3=s1-s2  # its also given difference from set two
s1.difference_update(s2)
print(s1)
print(s2)
# print(s3)