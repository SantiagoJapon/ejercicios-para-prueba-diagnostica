edad = int(input("que edad tienes?  "))
income = float(input("¿Cuales son tus ingresos mensuales?"))
if edad > 16 and income >= 1000:
    print("Tienes que cotizar")
else:
    print("No tienes que cotizar")