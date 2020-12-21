#Lists
my_list=["hello",1,66.6,"Sergey",5,66,79,69,420]

print("The Length Is: " + str(len(my_list)))

my_str="2375672465297435692445"
print("The Length Is: " + str(len(my_str)))

my_list.append("wow")
my_list.append("sergey")
print(my_list)
print("The New Length Is: " + str(len(my_list)))

my_list.insert(3,99)
print(my_list)

my_list.pop(3)
print(my_list)