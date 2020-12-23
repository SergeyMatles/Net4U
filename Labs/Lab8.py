from random import randint
while(True):
    MENU=input("\nMenu:\n1.Printing 100 Numbers\n2.Check Fibo\n3.Radndint Number Until we get 12 or Count 10 Times\n")
    if (MENU=="1"):
        for i in range(101):
            print(i)

    elif (MENU=="2"):
        fibo=[]
        for i in range (7):
            fibo.append(int(input("Enter a Numbers: ")))
        if MENU == "1":
            TRUE = "True"
        for i in range(2, len(fibo)):
            print(fibo[i])
            print(fibo[i - 1])
            print(fibo[i - 2])
            print("\n")
            if fibo[i] != (fibo[i - 1] + fibo[i - 2]):
                TRUE = "False"
                break
        if TRUE == "True":
            print("Its A Fibo")
        else:
            print("Its Not a Fibo")

    elif(MENU=="3"):
        COUNTER = 0
        while (COUNTER<11):
            NUM=randint(1,12)
            print("\nRound " + str(COUNTER) + " The Number: "+ str(NUM))
            COUNTER=COUNTER+1
            if (NUM==12):
                break
    else:
        print("\nEnter 1-3 Only")
        continue
    exit=input("\nDo you want to exit?\nYes/No\n")
    if (exit=="Yes"):
        print("\n\nBye Bye")
        break