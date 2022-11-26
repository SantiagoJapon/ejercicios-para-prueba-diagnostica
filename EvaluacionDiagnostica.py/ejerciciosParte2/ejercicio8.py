precio = input("Introduce el precio del producto con dos decimales:  ")
print(precio[:precio.find('.')], 'dolares y', precio[precio.find('.')+1:], 'centavos')