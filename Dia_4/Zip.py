nombres = ["Fran","Rama","Ziima","Santi","Chiro","Ivo"]
kills = [12,20,22,21,5,0]
apodos = ["Bondiola","Rama","Ziima","Bane","Device","Ark"]

resultados = list(zip(nombres,kills,apodos))
print(resultados)

for nombre,kills,apodo in resultados:
    print(f"{nombre} alias {apodo} hizo {kills} kills.")

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

informacion = list(zip(capitales,paises))

for capital,pais in informacion:
    print(f"La capital de {pais} es {capital}")

