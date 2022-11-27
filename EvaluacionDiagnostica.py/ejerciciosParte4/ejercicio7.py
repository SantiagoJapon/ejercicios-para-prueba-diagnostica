numero = int(input("Que altura deseas que tenga (entero positivo): "))
for i in range(1, numero+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")