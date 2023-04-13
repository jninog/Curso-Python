#try...  except...else...finally

try:
    numero1 = 5
    numero2 = 0
    division = numero1/numero2
    print(division)
except:
    print("Ha habido un error")

#zeroDivisoronErro

try:
    numero1 = 5
    numero2 = 2
    division = numero1/numero2
    print(division)
except ZeroDivisionError:
    print("Error, division entre cero")
except:
    print("Ha habido un error")
    
#else
try:
    numero1 = 5
    numero2 = 2
    division = numero1/numero2
    print(division)
except ZeroDivisionError:
    print("Error, division entre cero")
except:
    print("Ha habido un error")
else:
    print("La division funcionó correctamente")
    
#finnaly

try:
    numero1 = 5
    numero2 = 0
    division = numero1/numero2
    print(division)
except ZeroDivisionError:
    print("Error, division entre cero")
except:
    print("Ha habido un error")
else:
    print("La division funcionó correctamente")
finally:
    print("Esta prueba se ha finalizado")
    