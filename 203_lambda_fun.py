#lambda function example
# lambda paramter : expression  
cube = lambda num:num*num*num

square = lambda num :num*num

add= lambda a,b :a+b 

kgTogram = lambda kg : kg*1000

greatNumber= lambda a,b : a if a>b else b 

greatNumberThree= lambda a,b,c : a if a>b and a>c else b  if b>c else c

evenOdd = lambda num : "even" if num%2==0  else "odd"

posNag= lambda num : "postive" if num>0 else "nagatve" if num<0 else "zero"

evenlist = lambda lst : [n*n for n in lst if n%2==0]


multipleOf5 = lambda lst : [n for n in lst if n%5==0]

# evenSeries = lambda : [n for n in range(1,11) if n%2==0]

evenSeries = lambda a,b : [n for n in range(a,b+1) if n%2==0]

myPrint = lambda : print("hello students")


evenOddPrint = lambda num : print("even" if num%2==0  else "odd")

evenOddPrint(33)

res=myPrint()

l1= evenSeries(50,60)
print(l1)

l1= evenSeries(1,10)
print(l1)


print(multipleOf5([4,6,7,10,20,6]))

l1=[1,2,3,4,5,6]
l2= evenlist(l1)
print(l1)
print(l2)




print(posNag(0))
print(evenOdd(22))

print(greatNumberThree(120,67,900))
print(greatNumber(120,67))
print(add(4,9))
print(cube(3))
print(square(3))