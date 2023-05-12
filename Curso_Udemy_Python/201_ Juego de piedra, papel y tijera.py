# Juego piedra papel o tijera

import pandas as pd
import numpy as np

print('Bienvenidos al juego de piedra papel o tijera')

tijera=1
papel=2
piedra =3
respuesta_usuario = input('Elije si pones piedra papel o tijera ').lower()

if respuesta_usuario == 'tijera':
    valor_usuario= tijera
elif respuesta_usuario == 'papel':
    valor_usuario=papel
else:
    valor_usuario=piedra

ordenador = np.random.randint(1,3)

if ordenador == 1:
    valor_ordenador = tijera
elif ordenador == 2:
    valor_ordenador = papel
else:
    valor_ordenador = piedra

if valor_usuario == 1 and valor_ordenador ==2:
    print('Gana usuario con tijera')
elif valor_usuario == 2 and valor_ordenador==3:
    print('Gana usuario con papel')
elif valor_usuario == 3 and valor_ordenador ==1:
    print('Gana usuario con piedra')
elif valor_ordenador == 1 and valor_usuario ==2:
    print('Gana ordenador con tijera')
elif valor_ordenador == 2 and valor_usuario==3:
    print('Gana ordenador con papel')
elif valor_ordenador == 3 and valor_usuario ==1:
    print('Gana ordenador con piedra')
else:
    print('Empate')
    

print('Valor usuario '+ str(valor_usuario))
print('Valor ordenador '+ str(valor_ordenador))