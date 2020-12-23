#While Loops
from time import sleep
while(True):
    CHOOSE=input("Menu:\n1.Insert Number and ** it by 3\n2.Insert 4 Ips to a list and print it\n3.Insert 4 Entries to Dns_Dictionary and print it\n4.Check a string is Polindrom\n")

    if(CHOOSE=="1"):
        MUL=int((input("Enter a number to ** by 3:\n")))
        print("We Got:\n" + str(MUL**3))
    elif(CHOOSE=="2"):
        IPLIST=[]
        IPLIST.append(input("Enter New IP: "))
        IPLIST.append(input("Enter New IP: "))
        IPLIST.append(input("Enter New IP: "))
        IPLIST.append(input("Enter New IP: "))
        print("Your IP list Is:\n" + str(IPLIST))
    elif (CHOOSE=="3"):
        DICTD={}
        DICTD.update({input("Enter a URL: "):input("Enter IP: ")})
        DICTD.update({input("Enter a URL: "): input("Enter IP: ")})
        DICTD.update({input("Enter a URL: "): input("Enter IP: ")})
        DICTD.update({input("Enter a URL: "): input("Enter IP: ")})
        print("Your Dns_Dictionary List is:\n" + str(DICTD))
    elif (CHOOSE=="4"):
        POLI=input("Enter a word to test for Polindrom:\n")
        if(POLI == POLI[::-1]):
            print("It a Polindrom")
        else:
            print("Its Not a Polindrom")
    else:
        print("\nYou Must Choose Between 1-4\n")
    exit=input("Do You Want To Exit Type Yes/No\n")
    if (exit=="Yes" or exit=="yes"):
        break
print("\nThank You Bye Bye")