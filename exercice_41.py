num_1 = float(int(input("premier coter : ")))
num_2 = float(int(input("deuxieme coter : ")))
num_3 = float(int(input("troisieme coter : ")))

if num_1 == num_2 == num_3 : 
    print("Triangle equilateral")
elif num_1 == num_2 != num_3 : 
    print("triangle isocele")
elif num_1 != num_2 != num_3 :
    print ("triangle scalene")
