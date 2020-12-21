Dict1={"Serg":100,"Idan":200,"Dude":300,"Avi":400,"Ron":500}
print(Dict1)
print("Sum Of First and Last: " + str(Dict1["Serg"]+Dict1["Ron"]))
summary=Dict1["Serg"]+Dict1["Ron"]
Dict1.update({"Aviv":summary})
print(Dict1)
print("The number of entries: " + str(len(Dict1)))
print("Idan" in Dict1)
