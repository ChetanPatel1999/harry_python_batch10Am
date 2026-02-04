#make a project which check clube entry if your age above then 18 so enter
# in club then display menu 3,4 and you order any one item then display bill
# if your age less then 18 so diractaly diplay you are not adult try after some year.

age =int (input("enter your age : "))#16
if age>=18:
    print("welcome to club ! ")
    print("club menu :")
    print("1. sandwitch : 150")
    print("2. manchurian : 120")
    print("3. burger : 80")
    order=int(input("please order : "))
    match order:
        case 1: print("your sandwitch is order please pay 150 rs ")
        case 2: print("your manchurian is order please pay 120 rs ")
        case 3: print("your burger is order please pay 80 rs ")
        case _: print("wrong input ! please enter 1 to 3 ")

else:
    print(f"you are not adult please try after {18-age} year")    