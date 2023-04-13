try:
    numero1 = 6
    numero2 = 3
    numero3 = 3
    resta = numero2 - numero3
    operacion = numero1/resta
    print(operacion)
except ZeroDivisionError:
    print("Error, division entre cero")
except:
    print("Ha habido un error")
    
    
def operacion(numero1,numero2,numero3):
    resultado = numero1 / (numero2-numero3)
    return(resultado)
    
try:
    resultado = operacion(numero1,numero2,numero3)
    print(resultado)
except ZeroDivisionError:
    print("Error, Los dos ultimos numero no pueden ser iguales")