#  Bus Fare – Outer switch for city, nested switch for ticket type (normal, 
# express). (nested switch).
print("<---- bus fare app --->")
print("select city : ")
print("1. indore")
print("2. ujjain")
print("3. bhopal")
print("4. ratlam")
city=int(input("choose city : "))

match city:
    case 1:
        print("select ticket type for indore : ")
        print("1. normal : 50")
        print("2. express : 500")
        type=int(input("choose ticket type : "))
        match type:
            case 1:
                print("you selected normal ticket pay 50 rs")
            case 2:
                print("you selected express ticket pay 500 rs")
    case 2:
        print("select ticket type for ujjain : ")
        print("1. normal : 20")
        print("2. express : 300")
        type=int(input("choose ticket type : "))
        match type:
            case 1:
                print("you selected normal ticket pay 20 rs")
            case 2:
                print("you selected express ticket pay 300 rs")            