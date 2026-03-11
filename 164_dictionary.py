#wap to take dictonary data from user
student={}

num=int(input("enter student count : "))
for i in range(num):
    key=input(f"enter name student{i+1}: ")
    value=int(input(f"enter marks student{i+1}: "))
    # student[key]=value
    student.update({key:value})

print(student)