case = input("donner une case : ")
autre = float(input("donner lautre coter : "))


if case == "a" or case == "c" or case == "e" or case == "g":
    if autre == 1 or autre == 3 or autre == 5 or autre == 7 : 
        print("case noir")
    if autre == 2 or autre == 4 or autre == 6 or autre == 8:
        print ("case blanche")
if case == "b" or case == "d" or case == "f" or case == "h" :
    if autre == 1 or autre == 3 or autre == 5 or autre == 7 :
        print("case blanche")
    if autre == 2 or autre == 4 or autre == 6 or autre == 8 :
        print("clase noir")
