#call by reference and call by value

# call by reference
def fun(a): # 12
    print(a) # [12,67,23,88]
    a[3]=500
    print(a) # [12,67,23,500]


num=[12,67,23,88]
print("num = : ",num) # [12,67,23,88]
fun(num)
# fun(num.copy())
print("num = : ",num) #[12,67,23,500]