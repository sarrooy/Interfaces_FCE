#esto es un comentario 
inicio = "S"
while( inicio == "S"):
    print("escribe tu edad =")
    age = int( input())
    año = 2024 - age
    print("naciste en el año ", año)
    retorno = input("deseas comenzar de nuevo? S/N")
    if retorno == "S" or retorno =="s":
        print("escribiste S")
        inicio = "S"
    else:
        print("seleccionaste N")
        inicio = "N"
else:
    print("bye")            