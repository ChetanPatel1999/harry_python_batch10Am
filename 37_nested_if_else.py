# Write a program to read the age of a candidate and country ,then determine whether he 
# is eligible to cast his/her own vote in india or not. 
country=input("enter your country : ")
if country=="india":
    age=int(input("enter your age : "))
    if age>=18:
        print("you can vote in india")
    else:
        print("you are not eligibel for voting in india")    
        print(f"try after {18-age } year") 
else:
    print("you are not indian")           