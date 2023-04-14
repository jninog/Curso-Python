#Tkinter Componente entry (entrada de datos por teclado)

import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

# componente entry

entrada = tkinter.Entry(raiz)
entrada.config(justify="center",show="*")
entrada.config(bg="blue",width=400,height=300)
entrada.pack()


raiz.mainloop()