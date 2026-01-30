# rock paper scissor game
import random
user=input("enter your choise : \n1. rock \n2. paper\n3. scissor \nenter : ")

computer=random.choice(["rock","paper","scissor"])

if(user==computer):
    print("math is draw")


