# wap to take short name of state and print full name
state=input("enter state short name : ") #mn
match state:
    case "mp":print("madhya-pradesh")
    case "up":print("uttar-pradesh")
    case "rj":print("rajsthan")
    case "mh":print("maharastra")
    case "jk":print("joomu kashmire")
    case _:print("wrong short name please correct them")
