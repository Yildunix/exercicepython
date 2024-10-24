plus_litre = float(input('Combien avez vous de contenant de plus de 1L: ' ))
moins_litre = float(input('Combien avez vous de contenant de moins de 1L :'))

total = ( plus_litre * 0.25) + (moins_litre * 0.10)

print(f'total des produits remboursable : {total} $')