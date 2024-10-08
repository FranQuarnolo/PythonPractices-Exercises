from random import *

#RANDINT - arroja un numero aleatorio
aleatorio = randint(1,100)
print(aleatorio)


#ROUND - tira un valor aleatorio con decimales
unico = round(uniform(1,100), 2)
print(unico)

#RANDOM - elije un aleatorio entre 0 y 1. Siempre da una fraccion de 1 entero
numero = random()
print(numero)

#CHOICE - permite trabajar con una seleccion aleatoria dentro de una lista
colores = ["verde","azul","rojo","amarillo","violeta"]
color = choice(colores)
print(color)

#SHUFLE - altera de manera random el orden de los items de una lista.No se puede usar con string porque son inmutables
mazo = list(range(5,50,5))
shuffle(mazo)
print(mazo)

