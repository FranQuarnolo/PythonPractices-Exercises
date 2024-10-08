from Dia_4.Loop_For import nombre, letra

monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas.")
    monedas -= 1
else:
    print(f"Se me acabaron las monedas")

respuesta = "s"

while respuesta == "s":
    respuesta = input("Quieres seguir? s/n \n")
else:
    print("Gracias")

nombre = input("Tu nombre: \n")

for letra in nombre:
    if letra == "f":
        break
    print(letra)


