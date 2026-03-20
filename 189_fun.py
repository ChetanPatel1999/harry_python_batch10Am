#function with parameter
def add(a,b):
    c=a+b
    print(f"addition of {a} and {b} = {c}")
    # print(f"addition of %.1f and %.1f = %.1f"%(a,b,c))


add(4.2,6.4)
add(12,6)
add(2,7)
add(10,20)

add("ram","sharma")
add([12,34],[5,7])