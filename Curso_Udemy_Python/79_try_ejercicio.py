try:
    numero1 = 5
    numero2 = 4
    numero3 = 2
    resta = numero2 - numero3
    operacion = numero1/resta
    print(operacion)
except ZeroDivisionError:
    print("Error, division entre cero")
except:
    print("Ha habido un error")