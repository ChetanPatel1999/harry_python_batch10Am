def isPrime(num):
    c=0
    for i in range(1,num+1):
        if num%i==0:
          c+=1
    if c==2:
        return True
    else:
        return False

def rangePrime(s,e):
    for num in range(s,e+1): # i=2
        if isPrime(num):
            print(num,end=" ")


print("\nprime number 1 to 20 : ")
rangePrime(1,20)

print("\nprime number 50 to 100 : ")
rangePrime(50,100)



