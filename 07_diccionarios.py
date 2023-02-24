## Diccionarios ## 

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"nombre":"Julian",'Apellido':'Niño','Edad':29,1:'Python'}
print(my_other_dict)
print(type(my_other_dict))

my_dict = {
    "nombre":"Julian",
     'Apellido':'Niño',
     'Edad':29,
     'Lenguajes':{'Python','C#','BD'},
     1:1.71
}

print(len(my_dict))
print(my_other_dict)

print(my_dict['nombre'])

my_dict['nombre'] = 'Juan'
print(my_dict["nombre"])

print(my_dict[1])

my_dict['Calle'] = 'cre 31'
print(my_dict)

del my_dict['Calle']
print(my_dict)

print('Apellido' in my_dict)
print('Juan' in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())


my_new_dict = my_other_dict.fromkeys(('nombre',1))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict,('Julian','Niño'))
print(my_new_dict)