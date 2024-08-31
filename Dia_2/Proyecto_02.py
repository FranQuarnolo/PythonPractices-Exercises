nombre= input('Dime tu nombre: ')
ventas= int(input(f'Cuanto has vendido este mes {nombre}? \n'))

total = round(ventas*13/100, 2)

print(f"Ok {nombre} este mes ganaste ${total} de comisiones")