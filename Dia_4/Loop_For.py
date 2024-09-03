lista = ["Rama","Santi","Agus","Ziima"]
letra_inicio = input("Ingresa una letra:")
for nombre in lista:
    if nombre.lower().startswith(letra_inicio.lower()):
        print(f"El nombre {nombre} SI comienza con {letra_inicio}.")
    else:
        print(f"El nombre {nombre} NO comienza con {letra_inicio}.")


palabra = "python"
for letra in palabra:
    print(letra)

