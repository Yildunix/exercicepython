date = int(input("mettez un mois : "))
jour = float(input("mettre le jour du mois :"))

if date == "janvier" : 
    jour < 31
elif date == "fevrier" :
    jour <29
elif date == "mars" :
    jour < 31
elif date == "avril":
    jour <30
elif date == "mai":
    jour <31
elif date == "juin":
    jour <30
elif date == "juillet":
    jour <31
elif date == "aout":
    jour < 31 
elif date == "septembre":
    jour < 30
elif date == "octobre":
    jour < 31
elif date == "novembre":
    jour < 30
elif date == "decembre":
    jour <= 31
else :
    print("il ne fait pas partie du mois")

print(f"les jours est l'annee {jour}{date}")