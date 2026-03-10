#items() method of dictionary

student={'hindi': 80, 'math': 90, 'english': 70, 'science': 20}

items= student.items()
print(items)
student["math"]=35
print(items)

for i in items:
    print(i[0], "=", i[1])


for i in items:
    print(i)    

for key,value in items:
    print(key ,"=",value)    

