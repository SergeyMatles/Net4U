#Dictionary
Dict1={"www.google.com":"8.8.8.8","www.facebook.com":"7.7.7.7","www.youtube.com":["6.6.6.6","5.5.5.5"]}
print(Dict1)
Dict1.update({"www.net4u.com":"1.1.1.1"})
print(Dict1)

print("Length of Dictionary: " + str(len(Dict1)))
print(Dict1.values())

Dict1["www.google.com"]="8.8.4.4"
print(Dict1.values())

print("7.7.7.7" in Dict1.values())
