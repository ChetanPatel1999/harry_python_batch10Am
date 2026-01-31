# rock paper scissor game
import random
user=input("enter your choise : \n1. rock \n2. paper\n3. scissor \nenter : ")

computer=random.choice(["rock","paper","scissor"])

if user==computer:
    print("math is draw")
elif user=="rock" and computer=="scissor" or user=="paper" and computer=="rock" or user=="scissor" and computer=="paper":
    print(f"you win !{chr(1)} {user} beats {computer}")
else:
    print(f"computer win !{chr(1)} {computer} beats {user}")    



