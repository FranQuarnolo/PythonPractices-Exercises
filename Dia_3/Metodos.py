texto_prueba_1 = "Este es un texto pasado a mayus"
texto_prueba_2 = "Este es un texto pasado a minus"
texto_prueba_3 = "Este es un texto separado"

resultado_mayus = texto_prueba_1.upper()
resultado_minus = texto_prueba_2.lower()
resultado_separado = texto_prueba_3.split()

print(resultado_mayus)
print(resultado_minus)
print(resultado_separado)

a="Aprender"
b="Python"
c="es"
d="la"
e="Ondaaa"
f=" ".join([a,b,c,d,e])

print(f)

busqueda = texto_prueba_1.find("z")
print(busqueda)

reemplazo = texto_prueba_1.replace("mayus", "MAYUS")
print(reemplazo)

reemplazoXletra = texto_prueba_1.replace("e", "d")
print(reemplazoXletra)

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
reemplazo_1 = frase.replace("difícil","facil")
print(reemplazo_1)
reemplazo_2 = frase.replace("mala","buena")
print(reemplazo_2)

