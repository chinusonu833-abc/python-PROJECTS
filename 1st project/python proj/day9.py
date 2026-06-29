import random
items=["rocks","paper","scissor"]

computer=random.choice(items)

user=input("rock paper or scissor:").lower()

print("computer choices",computer)

if user == computer:
    print("match draw....!")
elif user =="rock"and computer =="scissor":
    print ("user winner!!!!!")
elif user=="paper"and computer =="rock":
    print("user winner!!!!!")
elif user =="scissor"and computer=="paper":
    print("user winner!!!!!")
else:
    print("computer winner!!")