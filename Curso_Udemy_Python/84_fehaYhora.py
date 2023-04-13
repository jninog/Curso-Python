from datetime import datetime

fechaYhora =datetime.now()
print(fechaYhora)

año=fechaYhora.year
print(año)

mes=fechaYhora.month
print(mes)

dia=fechaYhora.day
print(dia)

hora=fechaYhora.hour
print(hora)

minutos=fechaYhora.minute
print(minutos)

segundos=fechaYhora.second
print(segundos)

microsegun = fechaYhora.microsecond
print(microsegun)

print('La hora es {}:{}:{}'.format(hora,minutos,segundos))