#call by reference and call by value

# call by value 
def fun(a): # 12
    print(a) # 12
    a=67
    print(a) # 67


num=12
print("num = : ",num) # 12
fun(num)
print("num = : ",num) # 12