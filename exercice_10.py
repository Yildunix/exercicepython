import math     

demande = float(input('entrer un entiers a: '))
demande_2 = float(input('entrer un entiers b: '))

calcul =   demande_2 + demande, demande - demande_2 , demande_2 * demande , demande/demande_2 , math.log10(demande), demande ** demande_2

print(f'{calcul}')