## Condicionales##

my_conditions =  False

if my_conditions: 
    print('Se ejecuta la condicion del if')
    
my_conditions = 5*5
 
if my_conditions == 10: 
    print('Se ejecuta la condicion del segundo if')
    
if my_conditions > 10 and my_conditions <20: 
    print('ES mayor que 10 y menor que 20')
elif my_conditions ==25:
    print('Es igual a 25')
else:
    print('Es menor o igual que 10 o mayor o igual que 20 o distinto de 25')

print('la ejecución continua')
    


my_string = ''

if not my_string:
    print('Mi cadena es vacia')

if my_string == 'Mi cadena de textooo':
    print('Las cadenas de texto coinciden')