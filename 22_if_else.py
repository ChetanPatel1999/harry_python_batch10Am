# Write a program to read the age of a candidate and determine whether he is 
# eligible to cast his/her own vote
age=int(input("enter your age : ")) # 31
if age>=18:
    print("you can vote")
    print("please keep your voter card")
else:
    print("you can't vote")
    print(f"try after {18-age} year")
