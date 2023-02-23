## Strings

my_string = 'Mi String'
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string ))

My_new_string = 'Este es un string \n con salto de linea'
print(My_new_string)

My_new_string = 'Este es un string \t con salto de linea'
print(My_new_string)

## Formateo 

name, surname , age = 'Julian','Niño',29

print('Mi nombre es {} {} y mi edad es {}'.format(name,surname,age))
print('Mi nombre es %s %s y mi edad es %d'%(name,surname,age))
print(f'Mi nombre es {name} {surname} y mi edad es {age}')


#Desempaquetadi de caracteres

language = 'python'
a,b,c,d,e,f= language

print(a)
print(e)

#Division

language_slice = language[1:4]
print(language_slice)


language_slice = language[1:]
print(language_slice)


language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

#reverse languege

reversed_language = language[::-1]
print(reversed_language)


#funciones

print(language.capitalize())
print(language.upper())
print(language.count('t'))
print(language.isnumeric())
print(language.lower())
print(language.upper().isupper())