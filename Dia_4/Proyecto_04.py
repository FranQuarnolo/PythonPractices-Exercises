"""
1. Le pregunta al usuario su nombre
2. Pensa un numero entre el 1 y el 100
3. El usuario tiene 8 Intentos para adivinarlo
4. El programa responde 4 cosas:
    4.a: Si es numero es mayor a 100 o menor a 0 le dice que esta mal
    4.b: Si el numero que eligio el usuario es menor al seleccionado
    4.c: Si el numero que eligio el usuario es mayor al seleccionado
    4.d: Si el numero que eligio el usuario se le notifica que ha ganado y cuantos intentos le tomo acertarlo
"""
#
from random import *

usuario = input("Ingrese su nombre: \n")
print(f"Hola {usuario}!. Piensa un número entre el 1 y el 100. \nTienes 8 intentos.")

aleatorio = randint(1,100)
print(aleatorio)

intentos = 0
## mi Solucion

for intento in range(intentos):
    numero_usuario = int(input("Ingresa el número:"))
    if numero_usuario > 100 and numero_usuario < 0:
        print("El numero ingresado esta fuera de rango!")
    if numero_usuario < aleatorio:
        print("El número ingresado es menor")
    if numero_usuario  > aleatorio:
        print("El número ingresado es mayor")
    if numero_usuario == aleatorio:
        print(f"¡Excelente, Acertaste!, y solo te tomo {intento+1} intentos.")
        break
    if intento == intentos:
        print(f"Llegaste a la cantidad de intentos máxima. \n El número a adivinar era: {aleatorio}")

## solucion udemy
while intentos < 8:
    numero_usuario = int(input("Ingresa el número:"))
    intentos+=1

    if numero_usuario not in range(1,100):
        print("El numero ingresado esta fuera de rango!")
    if numero_usuario < aleatorio:
        print("EL numero es mas alto")
    if numero_usuario > aleatorio:
        print("EL numero es mas bajo")
    if numero_usuario == aleatorio:
        print(f"¡Excelente, Acertaste!, y solo te tomo {intentos} intentos.")
        break

if numero_usuario != aleatorio:
    print(f"Llegaste a la cantidad de intentos máxima. \n El número a adivinar era: {aleatorio}")


