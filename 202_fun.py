#python return multiple values by one function
def compute(num):
    square=num*num 
    cube=num*num*num
    return square , cube, num+num,[4,5,6],"string"


res=compute(4)

print(res)

for num in res:
    print(num)

