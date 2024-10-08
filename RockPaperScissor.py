import random
print("GAME RULES")
print("You have only 3 chances to loose the game")
print("R for Rock")
print("P for Paper")
print("S for Scissor")
print("Q for Quit")
print()
score=0
chance=3
c=True
while c:
    a=random.choice(["Rock","Paper","Scissor"])
    if chance:
        b=input("Enter R P S Q: ").upper()
        if b=="P" and a=="Rock":
            print("Congrats")
            score+=1
        elif b=="S" and a=="Paper":
            print("Congrats")
            score+=1
        elif b=="R" and a=="Scissor":
            print("Congrats")
            score+=1
        elif b=="Q":
            c=False
            print("Thank You")
            print("your score is: ",score)
        elif b not in["R","S","P","Q"]:
            print("Please see the game rules")
            print("R for Rock")
            print("P for Paper")
            print("S for Scissor")
            print("Q for Quit")
        else:
            print("Try again")
            chance-=1
    else:
        c=False
        print("Thank You")
        print("You loose the game and score is: ",score)