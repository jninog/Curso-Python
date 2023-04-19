#108. Componente messagebox para preguntar

import tkinter
from tkinter import messagebox


raiz = tkinter.Tk()
raiz.title("Mi programa")

# crear ventana para preguntao continuar
def preguntar():
    resultado = tkinter.messagebox.askquestion("¿Titulo de la pregunta","Quieres borrar fichero?")
    if(resultado =="yes"):
        print("Si, quiero borrar fichero")
    else:
        print("No, no quiero borrar el fichero")
    
boton = tkinter.Button(raiz,text="Pulsar para preguntar",command=preguntar)
boton.pack()


raiz.mainloop()