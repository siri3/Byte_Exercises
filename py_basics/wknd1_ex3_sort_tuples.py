#sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers.
#priority is that name > age > score

list =[]
print ("enter values. press ""enter"" at name prompt when you are done ")
while True: 
    name = input("enter name ")
    if name == "":
        break
    age = input("enter age in years ")
    height = input("enter height in cm ")
    t = (name, age, height)
    list.append(t)

list.sort()
print (list)