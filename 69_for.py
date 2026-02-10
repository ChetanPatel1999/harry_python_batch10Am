#  Write a program  to display the sum of the series [ 1+x+x^2/2!+x^3/3!+....].
x=5
n=10
fact=res=1
for i in range(1,n):
    fact*=i
    res+=(x**i)/fact
print("res = ",res)    
