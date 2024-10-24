compte = float(input("combien avez vous déposé sur votre compte : "))

taux_interet = (compte*(4/100)) + compte
taux_1a = (taux_interet * (4/100)) + taux_interet
taux_2a = (taux_1a * (4/100)) + taux_1a

print(f'le taux epargne pour 1 ans = {taux_interet:.2f} , pour 2 ans = {taux_1a:.2f}, pour 3 ans {taux_2a:.2f} ')