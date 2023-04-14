#Componente messagebox con información

import tkinter
from tkinter import messagebox

raiz = tkinter.Tk()
raiz.title("Mi programa")

def avisar():
    tkinter.messagebox.showinfo("Tutilo","Mensaje con la información")

#se crea Componente messagebox
boton = tkinter.Button(raiz,text="pulsa para aviso",command= avisar)
boton.pack()
raiz.mainloop()