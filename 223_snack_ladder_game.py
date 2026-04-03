from random import randint
#snake-start   s1  32   45  62  75  81  97
#snake-ending  s1  10   16  30  23  50  3
#lader -start  l1= 9   20   35   47   63 
#lader -end   l1= 80   44    70   95  76
def snack(P):
    s={32:10,45:16,62:30,75:23,81:50,97:3}
    if P in s:
        print("\nyou cut by snack at",P,"number that's why your pos now",s[P],)
        P=s[P]    
    return P

def ladder(P):
    s={9:80,20:44,35:70,47:95,63:76}
    if P in s:
        print("\nyou get  ladder at",P,"number that's why your pos now",s[P],)
        P=s[P]
    return P

def displyChart(P1,P2):
    for i in range(100,0,-1):
        if '0' in str(i):
            print()
        if i in [32,45,62,75,81,97]:
            print("    S",end="")
        elif i in [9,20 ,35,47,63]:
            print("    L",end="")    
        elif P1==P2==i:
            print("  p1p2",end="")    
        elif i==P1:
            print("   p1",end="")
        elif i==P2:
            print("   p2",end="")
        else:
            print("%5d"%i,end="")        
        


print("<-----------welcome to snake-ladder-Game-------------> ")
print("here participate two player :")
print("1. player1 (P1)")
print("2. player2 (P2)")
input("To start game press Enter : ")
P1=0
P2=0
while True:
    print("\n\nplayer 1 turn .....")
    input("press enter to roll dice : ")
    num=randint(1,6)
    print(f"\nwow ! you get {num} in dice roll ")
    P1=P1+num
    if P1>100:
        print("\nyour number above then 100 ....\n")
        P1=P1-num
    print("\n now P1 pos : ",P1)    
    P1=snack(P1)    
    P1=ladder(P1) 
    print("\n-------------- score in score - Chart ---------------")
    print("<----------------------------------------------------->")  
    displyChart(P1,P2)
    print("\n<----------------------------------------------------->")
    if P1==100:
        print("            ######----------------######")
        print("            yeee...!   palyer1 is Winner ")
        print("            ######----------------######")
        break


    print("\n\nplayer 2 turn .....")
    input("press enter to roll dice : ")
    num=randint(1,6)
    print(f"\nwow ! you get {num} in dice roll ")
    P2=P2+num
    if P2>100:
        print("\nyour number above then 100 ....\n")
        P2=P2-num
    print("\n now P2 pos : ",P2)    
    P2=snack(P2)    
    P2=ladder(P2) 
    print("\n-------------- score in score - Chart ---------------")
    print("<----------------------------------------------------->")    
    displyChart(P1,P2)
    print("\n<----------------------------------------------------->")
    if P2==100:
        print("           ######----------------######")
        print("           yeee...!   palyer2 is Winner ")
        print("           ######----------------######")
        break 