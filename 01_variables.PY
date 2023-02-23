#variable

my_string_variable = 'my string variable'

print(my_string_variable)


my_int_variable = 10
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)


my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

#concatenacion de variables en un print
print(my_string_variable,my_int_variable,my_bool_variable)
print('Este es el valor obtenido:',my_int_variable)

# funciones del sistema 
print(len(my_string_variable))

#Variables en una sola linea
name,surname,alias,age ='Julian','Niño','Juli',29
print ('Me llamo',name, surname,'Mi edad es',age)
"""first_name = input('What is your name: ')
age = input('how ol are you? ')
print(first_name)
print(age)"""

#cambiar tipo
name=35
age='JulianD'
print(type(name))
print(age)

#forzamos el tipo
address: str ='Mi direccion'
address = 32
print(type(address))