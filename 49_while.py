# Write a program to display factors of given number. 
# 12 => 1 2 3 4 6 12
# 15 => 1 3 5 15
num=int(input("enter a num : "))#15
i=1
print(f"factors of {num} : ",end="")
while i<=num:
    if num % i == 0:
      print(i,end=" ")
    i+=1

