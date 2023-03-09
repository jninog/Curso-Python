# Funciones

def saludar():
    print('Buenos días')
    
print(saludar())

def saludar(nombre):
    print('Buenos días '+nombre)
    
nombre = 'Julian'
    
print(saludar(nombre))

#Devuelve valor

def sumar(numero1,numero2):
    suma=numero1+numero2
    return suma

numero1 = 5
numero2 = 10

resultado = sumar(numero1,numero2)
print(resultado)

#paso de valor por referencia

colores = ['Azul','amarillo','balnco']

def incluir_color(colores,color):
    colores.append(color)

print('Introduzca color')    
color = input()
incluir_color(colores,color)
print(colores)
