decibel = float(int(input("donner le nombre de decibel : ")))

if decibel < 40 :
    print('il est inferieur a tout autre truc')
elif decibel == 40 :
    print("Chambre tranquille")
elif decibel < 70 :
    print("il est entre Chambre tranquille et Reveil")
elif decibel == 70 : 
    print("Reveil")
elif decibel < 106:
    print("entre Reveil et tondeuse a gazon")
elif decibel == 106 :
    print("tondeuse a gazon")
elif decibel < 130 : 
    print("Entre Tondeuse et Jackhammer ")
elif decibel == 130 :
    print("Jackhammer")
elif decibel > 130 :
    print("au dessus du bruit normal")
