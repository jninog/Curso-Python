#Expresiones regulaes (search, findall,split,sub)
import re

texto = 'Hola, mi nombre es Julian'

#search
resultado = re.search('y',texto)
print(resultado)

if(resultado):
    print('Cadena encontrada')
else:
    print('No se encontro la cadena de texto')
    
resultado2 = re.search('Julian$',texto) #si en la linea termina por Julian
print(resultado2)

resultado3 = re.search('^Hola',texto) # si hay linea en nuestra cadena de texto que empiece por Hola
print(resultado3)

resultado4 = re.search('mi.*es',texto) # . el punto es un comodin y el * es para que valide en toda la cadena   
print(resultado4)

#finall

texto2= '''EL coche de luis es Azul,
    el coche de antonio es blanco
    y el coche de Julian es Azul '''
    
resultad2_1= re.findall('coche.*Azul',texto2)
print(resultad2_1)

#spit divide cadena apartir de un patron

texto3= 'La silla es blanca y vale 80'

resultado3_1= re.split('\s',texto3)
print(resultado3_1)

#sub sustituye todas las concidencia de una cadena

texto4= 'La silla es blanca y vale 80'

resultado4_1= re.sub('blanca','Azul',texto4)
print(resultado4_1)



