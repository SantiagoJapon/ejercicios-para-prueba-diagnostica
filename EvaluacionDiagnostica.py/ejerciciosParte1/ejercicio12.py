barrasPan = int(input("Introduce el número de barras vendidas que no son frescas: "))
precio = 3.49 
descuento = 0.6
coste = barrasPan * precio * (1 - descuento)
print("El coste de una barra de pan es " + str(precio) + "€")
print("El descuento sobre una barra de pan no fresca " + str(descuento * 100) + "%")
print("El total a pagar es " + str(round(coste, 2)) + "€")