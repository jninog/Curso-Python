#Calculadora de propinas
#precio de facturas
#porcentaje de propinas
#personas a repartir

print('Bienvenidos a la calculadora de propinas')

factura = float(input("¿Cual es el importe de tu factura?"))   #recoger precio de factura por tecladoc
propina = int(input("¿Cual es el porcentaje de propina que quiere dejar?"))
personas = int(input('¿Entre cuantas personas hay que repartir la factura?'))

#calcular el importe total de la factura añadiendo la propina

importe_propina=(factura*propina)/100
factura_total = factura+importe_propina
importe_por_persona= factura_total/personas 
importe_redondeado=round(importe_por_persona,2) #redondea con dos decimales en este caso

print("EL importe a pagar por persona es " + str(importe_redondeado))
