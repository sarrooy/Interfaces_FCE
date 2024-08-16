#area de importacion de librerias
import tkinter as FCE 

window = FCE.Tk()
window.geometry("600x400")
window.title("App para caluclo de areas geometricas")
OP = 0    #definimos la variable que especifica el tipo de area a calcular

#area de definicion de funciones
def CUADRADO():
    print("cuadrado")
    global OP
    OP = 1
    L_valor1.config(text="valor de Lado del Cuadrado:")
    L_valor2.config(text="")
    E_Valor2.config(state="disable")

def TRUANGULO():
    print("TRUANGULO")
    global OP
    OP = 2
    L_valor1.config(text="valor de BASE del Triangulo:")
    L_valor2.config(text="valor de ALTURA del Triangulo:")
    E_Valor2.config(state="normal")
    
    
def RECTANGULO():
    print("RECTANGULO")
    global OP
    OP = 3
    L_valor1.config(text="valor de LADO1 del Rectangulo:")
    L_valor2.config(text="valor de LADO2 del Rectangulo:")
    E_Valor2.config(state="normal")
    
    
def CIRCULO():
    print("CIRCULO")  
    global OP
    OP = 4
    L_valor1.config(text="valor de Radio del Circulo:")
    L_valor2.config(text="")
    E_Valor2.config(state="disable")  
    
def RESULTADO():
    print("RESULTADO")  
    if OP == 1:
        lado =  int( E_Valor1.get() )
        AREA = lado*lado
        E_Res.delete(0,FCE.END)
        E_Res.insert(0,AREA)
    elif OP == 2:
        BASE = int( E_Valor1.get() )
        ALTURA = int( E_Valor2.get() )
        AREA = (BASE*ALTURA)/2
        E_Res.delete(0,FCE.END)
        E_Res.insert(0,AREA)
    elif OP == 3:
        LADO1 = int( E_Valor1.get() )
        LADO2 = int( E_Valor2.get() )
        AREA = LADO1*LADO2
        E_Res.delete(0,FCE.END)
        E_Res.insert(0,AREA)        
    elif OP == 4:
        RADIO =  int( E_Valor1.get() )
        AREA = (3.141564)*(RADIO**2)
        E_Res.delete(0,FCE.END)
        E_Res.insert(0,AREA)
    else:
        print("opcion no encontrada")
        E_Res.delete(0,FCE.END)
        E_Res.insert(0,"opcion no encontrada")
        
#definir los objetos GUI
L_Ins = FCE.Label(text="click en el boton para seleccionar la operacion a realizar")
B_Cuad = FCE.Button(text="CUADRADO", command=CUADRADO)
B_Trian = FCE.Button(text="TRUANGULO", command=TRUANGULO)
B_Rect = FCE.Button(text="RECTANGULO", command=RECTANGULO)
B_Circ = FCE.Button(text="CIRCULO", command=CIRCULO)

    #definimos los compoentes del layout derecho
L_Inst2 = FCE.Label(text="inserta los valores solicitados")
L_valor1 = FCE.Label(text="")
E_Valor1 = FCE.Entry(takefocus=True)    

L_valor2 = FCE.Label(text="")
E_Valor2 = FCE.Entry()

B_Res = FCE.Button(text="calcular Area", command=RESULTADO)
E_Res = FCE.Entry()
#area de generacion de GRID en ventana (LAYOUT de aplicacion)
L_Ins.grid(column=0, row=0, padx=2, pady=2)
B_Cuad.grid(column=0, row=1, padx=2, pady=2)
B_Trian.grid(column=0, row=2, padx=2, pady=2)
B_Rect.grid(column=0, row=3, padx=2, pady=2)
B_Circ.grid(column=0, row=4, padx=2, pady=2)
    #esctructura del Layput DERECHO
L_Inst2.grid(column=1, row=0, padx=2, pady=2)
L_valor1.grid(column=1, row=1, padx=2, pady=2)
E_Valor1.grid(column=1, row=2, padx=2, pady=2)

L_valor2.grid(column=1, row=3, padx=2, pady=2)
E_Valor2.grid(column=1, row=4, padx=2, pady=2)

B_Res.grid(column=1, row=5, padx=2, pady=2)
E_Res.grid(column=1, row=6, padx=2, pady=2)

#siempre una app GUI cierra con el comando:
window.mainloop()