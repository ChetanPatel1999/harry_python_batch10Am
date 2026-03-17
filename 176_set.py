# Keep All, But NOT the Duplicates 
s1={12,9,5,7,8}
s2={7,8,25,30,22}
# s3=s1.symmetric_difference(s2)
# s1.symmetric_difference_update(s2)
s3=s1^s2   # bitwise x-or is used to symmetric_difference
print(s1)
print(s2)
print(s3)
