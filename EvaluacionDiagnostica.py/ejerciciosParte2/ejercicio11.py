producto = input('que producto escogiste: ')
precio = float(input('Introducde el precio unitario: '))
unidades = int(input('cuantos vas a llevar: '))
print('{producto}: {unidades:3d} unidades x {precio:9.2f}$ = {total:11.2f}$'.
    format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))