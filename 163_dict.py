s1={"name":"ram","rno":102,"per":90}
s2={"name":"raj","rno":103,"per":50}
s3={"name":{"first":"sahaj","last":"sharma"},"rno":104,"per":80}
students={
       "s1":s1,
       "s2":s2,
       "s3":s3 }

print(students["s1"])
print(students["s3"]["name"]["first"])
print(students["s3"]["name"]["last"])
students["s3"]["name"]["last"]="chabra"
print(students)
# for key in students:
#     print(students[key]["rno"])
