#### Listas ####

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35,24,62,52,30,30,17]

print(my_list)
print(len(my_list))

my_other_list =  [35,1.77,'Brais','moure']

print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])

print(my_other_list.count('Brais'))
print(my_list.count(30))

edad, altura, nombre, apellido = my_other_list
print(nombre)

print(my_list+my_other_list)

##print(my_list * my_other_list) error

my_other_list.append('Raddar')
print(my_other_list)

my_other_list.insert(1,'azul')
print(my_other_list)

my_other_list.remove('azul')
print(my_other_list)

my_list.remove(30)
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)

del my_list[2] # elimina lista
print(my_list)

my_new_list = my_list.copy() #copia lista

my_list.clear() #limpia lista
print(my_list)
print(my_new_list)

my_new_list.reverse() ## ordena de final a inicio
print(my_new_list)

my_new_list.sort() #ordena la lista
print(my_new_list)

print(my_new_list[0:2])