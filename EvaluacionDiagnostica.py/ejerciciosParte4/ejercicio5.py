numero = int(input("Que altura quieres que tenga el triangulo (entero positivo): "))
for i in range(numero):
    for j in range(i+1):
        print("*", end="")
    print("")