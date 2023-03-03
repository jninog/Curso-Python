dicionario = {'Manzana':'Apple','Naranja':'Orange','Platano':'banana','limon':'lemon'}

print(type(dicionario))

print(dicionario['Naranja'])

dicionario['Piña']='Pineapple'

print(dicionario)

for clave,valor in dicionario.items():
    print('{} en ingles es {}'.format(clave,valor))