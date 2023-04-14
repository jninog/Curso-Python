#Componente filedialog (para preguntar por ficheros)

import tkinter
from tkinter import filedialog


raiz = tkinter.Tk()
raiz.title("Mi programa")

def abrirfichero():
    rutafichero = filedialog.askopenfilename(title="Abir un fichero")
    print(rutafichero)
#Crear metodo para abrir fichero

    
boton = tkinter.Button(raiz, text="Pulsar para empezar",command=abrirfichero)
boton.pack()


raiz.mainloop()