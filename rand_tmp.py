from random import randint
from time import sleep

print("Getting Random Numbers...\n")
sleep(2)
num1=randint(1,99)
num2=randint(1,99)

print("1st Number: " + str(num1) + "\n2nd Number: " + str(num2) + "\n")

if(num1==num2):
    print("Youre So Lucky You Have WON")
else:
    print("To Bad Try Again")