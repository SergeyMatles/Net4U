# For Loops
from time import sleep

print("Getting Class Info:\n------------------------")
for i in range(4):
    name=input("Enter Name: ")
    age=int(input("Enter Your Age: "))
    phone=input("Enter Phone Number: ")
    print("Printing Students Number " + str(i+1) + " Details...\n")
    sleep(2)
    print("Full Name: " + name + "\nAge: " + str(age) + "\nPhone Number: " + phone + "\n------------------------\n")