pesoPayaso = 112
pesoMunieca = 75

payasos = int(input("Cuantos payasos va a enviar: "))
muniecas = int(input("Cuantas muniecas va a eviar: "))

peso_total = pesoPayaso * payasos + pesoMunieca * muniecas

print("El peso final es de: " + str(peso_total))