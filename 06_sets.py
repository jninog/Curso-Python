### Sets ###

my_set = set()
my_other_set = {}


print(type(my_set))
print(type(my_other_set)) #inicialmente me dice que es un diccionario

my_other_set = {'Julian','Niño',35}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add('Niño2')
print(my_other_set) #Un set no es una estructura ordenada

my_other_set.add('Niño2')
print(my_other_set) #Un set no admite repetidos

print('niño' in my_other_set)
print('Niño' in my_other_set)

my_other_set.remove('Niño2')
print(my_other_set)

my_other_set.clear() #Elimina los registros
print(len(my_other_set))

del my_other_set
#print(my_other_set) noeta definido porque elimina el objeto

my_set = {'Julian','Niño',35}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {'SQL','BI#','Python'}
my_new_set = my_set.union(my_other_set)
print(my_new_set.union({'Java','Power BI'}))

print(my_new_set.difference(my_set))