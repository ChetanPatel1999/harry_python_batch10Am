# Write a program to check whether a value exists in dictionary or not. 
d1={"pen":40,"color":30,"book":50}

value = 30

# for key in d1:
#     if d1[key]==value:
#         print(f"{value} value is exist on {key} key")
#         break
# else:
#     print("value is not exist")    

if value in d1.values():
    print("yes exist")
else:
    print("not exist")    