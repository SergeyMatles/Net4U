#num=4567
num=int(input("Enter a number with 4 digits: "))
"""
Alafim=4
Meot=5
Asarot=6
Ahadot=7
"""

print("Alafim=" + str(num//1000))
print("Meot=" + str(num%1000//100))
print("Asarot=" + str(num%100//10))
print("Ahadot=" + str(num%10))