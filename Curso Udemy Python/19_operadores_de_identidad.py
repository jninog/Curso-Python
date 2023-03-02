frutas1 = ['manzana', 'pera']
frutas2 = ['manzana', 'pera']
frutas3 = frutas1

print(frutas3 is frutas1)

#adicionar elementos

frutas3.append('Naranjas')
print(frutas3 is frutas1)
print(frutas1)


print(frutas3 is not frutas1)