#Componente checkbutton (botón de verificación)

import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

# Componente checkbutton

def verificar():
    valor = check1.get()  #se captura el valor de la variable
    if (valor == 1):
        print("El check esta activo")
    else:
        print("El check esta desativado")

check1 = tkinter.IntVar()

boton1 = tkinter.Checkbutton(raiz,text="Opción 1",variable = check1, onvalue=1,offvalue=0,command=verificar)
boton1.pack()

raiz.mainloop()