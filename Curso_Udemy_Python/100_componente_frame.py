import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

#creamos componente Frame, permite incluir ottros componentes dentro del mismo

frame =tkinter.Frame(raiz)
frame.config(bg="blue",width=400,height=300)
frame.pack()

raiz.mainloop()