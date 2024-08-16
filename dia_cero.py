import tkinter as ttk

ventanaRaiz = ttk.Tk()


#espacio de difiniciones
def BorraTexto():
    print("esto se escribira al hacer click en boton borrar")
    textInput.delete(0, ttk.END)

def DefaultText():
    print("esta funcion escribe un texto por Default en el EntryText")
    textInput.insert(0,"Saludos en Viernes 9 de agosto")
    
def EnvioSaludo():
    print("esta funcion repite saludo de usuario en una LABEL")
    recibeSaludo.config(text= textInput.get()) 
#generacion de objetos de ventana
saludo1 = ttk.Label(text="escribe el saludo a enviar: ")
recibeSaludo = ttk.Label(text="")
textInput = ttk.Entry()
botonSaludo = ttk.Button(text="envair saludo", 
                         width=15,
                         height=5,
                         bg="black",
                         fg="red",
                         command=EnvioSaludo)
botonBorrar = ttk.Button(text="borrar mensaje",
                         command=BorraTexto)
botonDefault = ttk.Button(text="saludo predeterminado", command=DefaultText)
#espacio de agrupacion en ventana
saludo1.pack()
textInput.pack()
botonSaludo.pack()
botonBorrar.pack()
botonDefault.pack()
recibeSaludo.pack()
#fin del loop
ventanaRaiz.mainloop()

