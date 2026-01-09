#value display using string format method
name="chetan"
a=12
b=7
c=a+b
f=4.5
print("value of name = {}".format(name))
print("value of a = {}".format(a))
print("sum of {} and {} = {}".format(a,b,c))
print("sum of {0} and {1} = {2}".format(a,b,c))
print("sum of {1} and {1} = {1}".format(a,b,c))
print("sum of {2} and {1} = {0}".format(a,b,c))
print("sum of {x} and {y} = {z}".format(x=a,y=b,z=c))

