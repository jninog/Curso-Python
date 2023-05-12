
print('Bienvenidos al juego!! Para este juego debes responder a las pregunas solicitadas')

Pregunta1= input('¿Quieres ir a la derecha o izquierda? ').lower()
if Pregunta1 == 'izquierda':
    print('Fin, perdiste')
else:
    pregunta2= input('¿Quieres nadar o esperar? ').lower()
    if pregunta2 == 'nadar':
        print('Fin, has perdido')
    else:
        pregunta3 = input('Escoge un color rojo, azul o verde ').lower()
        if pregunta3 == 'rojo' or pregunta3 =='azul':
            print('Fin, has perdido')
        else:
            print('Has ganado!!')
            
    