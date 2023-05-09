from tkinter import*

ventana=Tk()
ventana.title('Calculadora') #titulo
ventana.geometry("395x400") #tamaño
ventana.resizable(False,False) #no se puede modificar el tamaño
ventana.configure(background='gray') #color de fondo

#variables
operacion=''
resultado=StringVar()

#funciones

#funcion limpiar caja de texto al ejecutar boton AC
def borrar():
    global operacion #aqui en la funcion recupera las variables y las limpia
    global resultado
    operacion=''
    pantalla.delete(0,END) #borrar desde la posición Cero hasta el final (END) de lo que tenga la pantalla

#funcion pulsar de los botones numericos
def pulsar(valor):
    global operacion #Recuperar valores de las variables
    global resultado #Recuperar valores de las variables
    operacion = operacion+str(valor)
    pantalla.delete(0,END)
    pantalla.insert(0,operacion)
    
#funcion calcular alojada en el boton =    
def calcular():
    global operacion #Recuperar valores de las variables
    global resultado #Recuperar valores de las variables
    try:
        resultado = str(eval(operacion))
    except:
        resultado='Error'
    finally:
        pantalla.delete(0,END)
        pantalla.insert(0,resultado)
    
    
#crear el campo de texto,donde se ponen los valores a evaludar
pantalla = Entry(ventana,font=('arial',20,'bold'),borderwidth=2)
pantalla.grid(row=0,column=0,columnspan=3,pady=5,padx=5) #situar la caja de texto en el lugar que deseamos

#crear boton de eliminar los resultados el AC
boton_reset= Button(ventana,text='AC',width=8,height=2,command=lambda:borrar()) #se cpnfigura la funcion de borrar en la parte de arriba
boton_reset.grid(row=0,column=3,pady=10) #.grid se muestra la configuración de los objetos creados, en este caso el button

#creación de los botones de la primera fila del 1 al 4
ancho= 8
alto=3
#boton1
boton1=Button(ventana,text='1',width=ancho,height=alto,command=lambda:pulsar('1')) # se crean los botones y se le agrega la funcion pulsar creada anteriormente
boton1.grid(row=1,column=0,padx=5,pady=5)

#boton2
boton2=Button(ventana,text='2',width=ancho,height=alto,command=lambda:pulsar('2')) # se crean los botones y se le agrega la funcion pulsar creada anteriormente
boton2.grid(row=1,column=1,padx=5,pady=5)

#boton3
boton3=Button(ventana,text='3',width=ancho,height=alto,command=lambda:pulsar('3')) # se crean los botones y se le agrega la funcion pulsar creada anteriormente
boton3.grid(row=1,column=2,padx=5,pady=5)

#boton2
boton4=Button(ventana,text='4',width=ancho,height=alto,command=lambda:pulsar('4')) # se crean los botones y se le agrega la funcion pulsar creada anteriormente
boton4.grid(row=1,column=3,padx=5,pady=5)

#creación de los botones de la segunda fila del 5 al 8
#boton5
boton5=Button(ventana,text='5',width=ancho,height=alto,command=lambda:pulsar('5')) # se crean los botones y se le agrega la funcion pulsar creada anteriormente
boton5.grid(row=2,column=0,padx=5,pady=5)
#boton6
boton6=Button(ventana,text='6',width=ancho,height=alto,command=lambda:pulsar('6')) # se crean los botones y se le agrega la funcion pulsar creada anteriormente
boton6.grid(row=2,column=1,padx=5,pady=5)
#boton7
boton7=Button(ventana,text='7',width=ancho,height=alto,command=lambda:pulsar('7')) # se crean los botones y se le agrega la funcion pulsar creada anteriormente
boton7.grid(row=2,column=2,padx=5,pady=5)
#boton8
boton8=Button(ventana,text='8',width=ancho,height=alto,command=lambda:pulsar('8')) # se crean los botones y se le agrega la funcion pulsar creada anteriormente
boton8.grid(row=2,column=3,padx=5,pady=5)

#creación de los botones de la tercera fila (9,0.+)

#boton9
boton5=Button(ventana,text='9',width=ancho,height=alto,command=lambda:pulsar('9')) # se crean los botones y se le agrega la funcion pulsar creada anteriormente
boton5.grid(row=3,column=0,padx=5,pady=5)
#boton0
boton0=Button(ventana,text='0',width=ancho,height=alto,command=lambda:pulsar('0')) # se crean los botones y se le agrega la funcion pulsar creada anteriormente
boton0.grid(row=3,column=1,padx=5,pady=5)
#boton (.)
botonpunto=Button(ventana,text='.',width=ancho,height=alto,command=lambda:pulsar('.')) # se crean los botones y se le agrega la funcion pulsar creada anteriormente
botonpunto.grid(row=3,column=2,padx=5,pady=5)
#boton(+)
botonSuma=Button(ventana,text='+',width=ancho,height=alto,command=lambda:pulsar('+')) # se crean los botones y se le agrega la funcion pulsar creada anteriormente
botonSuma.grid(row=3,column=3,padx=5,pady=5)

#creación de los botones de la cuarta fila (9,0.+)

#boton (-)
botonResta=Button(ventana,text='-',width=ancho,height=alto,command=lambda:pulsar('-')) # se crean los botones y se le agrega la funcion pulsar creada anteriormente
botonResta.grid(row=4,column=0,padx=5,pady=5)
#boton (*)
botonMulti=Button(ventana,text='*',width=ancho,height=alto,command=lambda:pulsar('*')) # se crean los botones y se le agrega la funcion pulsar creada anteriormente
botonMulti.grid(row=4,column=1,padx=5,pady=5)
#boton (/)
botonDivi=Button(ventana,text='/',width=ancho,height=alto,command=lambda:pulsar('/')) # se crean los botones y se le agrega la funcion pulsar creada anteriormente
botonDivi.grid(row=4,column=2,padx=5,pady=5)
#boton(=)
botonIgual=Button(ventana,text='=',width=ancho,height=alto,command=lambda:calcular()) # se crean los botones y se le agrega la funcion pulsar creada anteriormente
botonIgual.grid(row=4,column=3,padx=5,pady=5)

ventana.mainloop()

