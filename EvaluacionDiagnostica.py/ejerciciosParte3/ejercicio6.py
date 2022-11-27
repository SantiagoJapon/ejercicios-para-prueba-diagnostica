nombre = input("¿Cómo te llamas? ")
genero = input("¿Cuál es tu sexo (M o H)? ")
if (genero == "M" and nombre.lower() < 'm') or (genero == "H" and nombre.lower() > 'n'):
    group = "A"
else:
    group = "B"
print("Tu grupo es " + group)