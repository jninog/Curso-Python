#Componente Button (botón para ejecutar una acción)

import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

# componente boton
#definimos la funcion accion
def accion():
    print("Hola Mundo")

boton = tkinter.Button(raiz,text="Ejecutar",command=accion)
boton.config(fg="Blue")
boton.pack()


raiz.mainloop()