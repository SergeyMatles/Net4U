from random import randint
from time import sleep
print("Lets Gamble\nEach Round Cost 3 ILS\n")
PMON=int(input("How Much Money Do You Want To Play With?\n"))
print("You Can Play:" + str(PMON//3) + " Times\nAnd Your Change is: " + str(PMON%3) + "ILS")
Winnings=0
sleep(2)

for i in range (PMON//3):
    sleep(1)
    print("\nRound Number" + str(i+1) + ":")
    Cube1=(randint(1,6))
    Cube2=(randint(1,6))
    print("Cube 1: " + str(Cube1) + "\nCube 2: " + str(Cube2))
    if (Cube1==Cube2):
        if (Cube1==6):
         Winnings=Winnings+1000
        else:
         Winnings=Winnings+100
    elif (Cube2==2):
     Winnings=Winnings+40
    elif (Cube1==1):
     Winnings=Winnings+20
sleep(1)
print("\nYour Winnings Are: " + str(Winnings) + " ILS")