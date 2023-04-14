#105. Componente radiobutton (botón de opción multiple

import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

#Componente Radiobutton

def selecciionar():
    print("La opción selecionada es {}".format(opcion.get()))
    
opcion = tkinter.IntVar()

radiobutton1= tkinter.Radiobutton(raiz,text="Opción 1",variable=opcion,value=1,command=selecciionar)
radiobutton1.pack()

radiobutton2= tkinter.Radiobutton(raiz,text="Opción 2",variable=opcion,value=2,command=selecciionar)
radiobutton2.pack()

radiobutton3= tkinter.Radiobutton(raiz,text="Opción 3",variable=opcion,value=3,command=selecciionar)
radiobutton3.pack()

raiz.mainloop()