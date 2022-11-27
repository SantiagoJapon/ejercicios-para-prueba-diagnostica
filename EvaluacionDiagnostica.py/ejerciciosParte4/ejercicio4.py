monto = float(input("Cantidad a invertir:  "))
interest = float(input("Interés porcentual anual: "))
years = int(input("Anios: "))
for i in range(years):
    monto *= 1 + interest / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(monto, 2)))