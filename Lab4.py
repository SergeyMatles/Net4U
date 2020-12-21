ListA=["Sergey Mat",25,"Sergey@Gmail.com","05445445545"]
print("Full Name: "+ ListA[0] + "\nAge: " + str(ListA[1]) + "\nEmail: " + ListA[2] + "\nPhone: " + ListA[3])

ListB=["192.168.0.0, 192.168.0.1"]
print(ListB)
ListB.append("192.168.0.2")
ListB.append("192.168.0.3")
ListB.append("192.168.0.4")
print(ListB)
ListB.pop(2)
print("Ip List Length is: " + str(len(ListB)) + "\nIps in the list:" + str(ListB))
