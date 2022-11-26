inversion = float(input("Ingresa tu primera inversion: "))
interes = 0.04

balance_1 = inversion * (1 + interes)
print("Aqui el balance tras el primer anio: "+ str(round(balance_1, 2)))

balance_2 = balance_1 * (1 + interes)
print("Aqui el balance tras el segundo anio: " + str(round(balance_2, 2)))

balance_3 = balance_2 * (1 + interes)
print("Aqui el balance tras el tercer anio: " + str(round(balance_3, 3)))
