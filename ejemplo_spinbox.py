from tkinter import ttk
import tkinter as tk

pago= 0
def CambioTemp():
    print("actualiza temp")
    temp = float(spin_temp.get()[:2])
    global pago
    costo = temp*pago
    etiqueta_costo.config(text=f"costo de litros de gasolina: {costo}")
    if temp <= 17:
        consumo = "Bajo"
    elif temp <= 24:
        consumo = "Medio"
    elif temp <= 30:
        consumo = "Alto"
    etiqueta_consumo.config(text=f"Consumo de energía: {consumo}.")

def sel():
    global pago
    print("seleccion")
    seleccion = int( var.get() )
    if seleccion == 1:
        pago = 25.50
    elif seleccion == 2:
         pago = 24.56
    else:
        pago = 23.00
    etiqueta_pago.config(text=f"costo de gas selec = {pago}")

def Toggle():
    print("checkbutton")
    EstadoCombo = combo.get()
    etiqueta_comboBox.config(text= EstadoCombo)
    if CheckVar.get() == 1:
        print("Checkbutton is selected")
    else:
        print("Checkbutton is deselected")

root = tk.Tk()
root.config(width=300, height=300)
root.title("Termostato virtual")
#agregamos el TAB-CONTROL
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
#las instanciamos en ventana
tabControl.add(tab1, text='App Gasolina')
tabControl.add(tab2, text='App Temperatura')
tabControl.add(tab3, text='Areas')

tabControl.pack(expand=1, fill="both")

var =tk.IntVar() #IntVar()
CheckVar = tk.IntVar()
etiqueta_temp = ttk.Label(tab1, text="Temperatura:")
etiqueta_temp.place(x=20, y=30, width=100)

etiqueta_consumo = ttk.Label(tab1)
etiqueta_consumo.place(x=20, y=80)

spin_temp = ttk.Spinbox(tab1,
                        from_=5, to=30, 
                        increment=0.05, 
                        state="readonly",
                        format="%.2fºC",
                        command=CambioTemp)
spin_temp.place(x=105, y=30, width=70)

etiqueta_costo = ttk.Label(tab1)
etiqueta_costo.place(x=20, y=100)

R1 = tk.Radiobutton(tab1, text="Gasolina ROJA", variable=var, value=1, command=sel)
R1.place(x=20, y=130)

R2 = tk.Radiobutton(tab1, text="Gasolina VERDER", variable=var, value=2, command=sel)
R2.place(x=20, y=160)

R3 = tk.Radiobutton(tab1, text="DIESEL", variable=var, value=3, command=sel)
R3.place(x=20, y=190)

etiqueta_pago = ttk.Label(tab1, text="")
etiqueta_pago.place(x=20, y=210)

#primer Widget de la tab2
checkbutton = tk.Checkbutton(tab2, 
                             text="Habilitacion de Caracteristicas", 
                             variable=CheckVar, 
                             onvalue=1, 
                             offvalue=0, 
                             command=Toggle)
checkbutton.place(x=20, y=30)

# Setting options for the Checkbutton
checkbutton.config(bg="lightgrey", fg="blue", font=("Arial", 12), 
                   selectcolor="green", relief="raised", padx=10, pady=5)

# Adding a bitmap to the Checkbutton
checkbutton.config(bitmap="info", width=20, height=2)
# Calling methods on the Checkbutton
checkbutton.flash()

#comboBOX
combo = ttk.Combobox(tab2,
                     state="readonly",
                     values=["Python", "C", "C++", "Java"]
                     )
combo.place(x=20, y=60)

etiqueta_comboBox = ttk.Label(tab2)
etiqueta_comboBox.place(x=20, y=90)

root.mainloop()