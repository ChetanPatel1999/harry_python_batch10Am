#Write a program to count how many elements in an array are prime and how many are not prime. 
l1=[12,5,7,56,17,23,66,88]
primeCount=0
notPrimeCount=0
prime=[]
notPrime=[]
for num in l1:
    c=0
    for i in range(1,num+1):
        if num%i==0:
            c+=1
    if c==2:
        primeCount+=1
        prime.append(num)
    else:
        notPrimeCount+=1
        notPrime.append(num)  
print("total prime count : ",primeCount)          
print("total not prime count : ",notPrimeCount)          
print("prime list : ",prime)          
print("not prime list : ",notPrime)          
         

