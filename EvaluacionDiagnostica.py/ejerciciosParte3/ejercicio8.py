bonificacion = 2400
muyMalo = 0
mejor = 0.4
excelente = 0.6
puntos = float(input("Introduce tu puntuación: "))


if puntos == muyMalo:
    nivel = "muyMalo"
elif puntos == mejor:
    nivel = "mejor"
elif puntos >= 0.6:
    nivel = "excelente"
else:
    nivel = ""


if nivel == "":
    print("Esta puntuación no es válida")
else:
    print("Tu nivel de rendimiento es %s" % nivel)
    print("Te corresponde cobrar %.2f€" % (puntos * bonificacion))