#Prices
Agva=3
Melaf=2
Cok=5
Chick=20
Mam=17
#Shopping Options
Tomato=int(input("How many Tomatos would you like?"))
Cucambers=int(input("How many Cucambers would you like?"))
Cokes=int(input("How many Cokes would you like?"))
Chicken=int(input("How many Chikens would you like?"))
#Print Shoping List
print("Your Shoping List:\n-----------------\nTomatos: " + str(Tomato) + "\nCucambers: " + str(Cucambers) + "\nCokes: " + str(Cokes) + "\nChicken: " + str(Chicken))
#Total Price
sum1=Agva*Tomato + Cucambers*Melaf + Cokes*Cok + Chicken*Chick
sum2=(sum1*Mam)//100 + sum1
print("Your Total Price Before Taxes: " + str(sum1))
print("Your Total Price After Taxes: " + str(sum2))
