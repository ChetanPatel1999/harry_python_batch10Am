#Variable-Length Arguments  
# *args -These are Non-Keyword Arguments 

def add(c,b,*a):   # variable length argument must be last
    print(c)
    print(b)
    sum=0
    for num in a:
        sum+=num
    print("sum = ",sum)    
   


# add(23)
add(23,89)
add(23,89,10)
add(23 ,89 ,10 ,20)
add(23.34 ,89.12 ,10.3 ,20.5)