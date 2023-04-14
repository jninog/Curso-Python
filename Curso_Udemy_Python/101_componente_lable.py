# tkinter - componente label

import tkinter

raiz = tkinter.Tk()
raiz.title("MI programa")

#cramos componente label

texto = "Hola Mundo"
etiqueta = tkinter.Label(raiz,text=texto)
etiqueta.config(fg="blue",bg="lightgrey",font=("cortana",30))
etiqueta.pack()

raiz.mainloop()