#1.Pedirle al usuario que ingrese un texto
#2.Ingresar 3 letras a su elección
#3.El programa tiene que procesar:
#   1.Cuantas veces aparece cada letra. Almacenar en una lista. Y contar
#   2.Cuantas palabras hay en total. Metodo de strings que permite transformar palabras en una lista para calcular su longitud.
#   3.Primera letra del texto y cual es la ultima
#   4.Como quedaria el texto invirtiendo las palabras
#   5.Aparece "python" en el texto
#1
texto = input("Porfavor ingrese su texto:\n")
print(f"TEXTO:\n \b'{texto}'")
texto.lower()

#TEXTO EJEMPLO
#Me lo oiras decir muchas veces: la importancia de los detalles es capital...

#2
print("LISTADO DE LETRAS: ")
listado_letras =[]
for i in range (3):
    letra = input(f"Ahora ingrese 1 letra:\n").lower()
    listado_letras.append(letra)
print(f"Listado de letras:\n \b{listado_letras}\n")
#3
#3.1
print("CANTIDAD DE LETRAS:")
apariciones=[]
for i in range (3):
    aparicion = texto.count(listado_letras[i])
    apariciones.append(aparicion)

for i in range (3):
    print(f"La letra '{listado_letras[i].upper()}' se encontró:\n {apariciones[i]} veces.")

#3.2
print("CUANTAS PALABRAS HAY EN TOTAL:")
palabras = texto.split()
print(f"Cantidad de palabras: {len(palabras)}")

#3.3
print(f"Primera letra del texto es: {texto[0]}")
print(f"Ultima letra del texto es: {texto[-1]}")

#3.4
print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = " ".join(palabras)
print(f"El texto invertido quedaria como: {texto_invertido}")

#3.5
print("APARECE PYTHON?")
aparece = 'python' in texto.lower()
if aparece == True:
    print("Si aparece")
else:
    print("No aparece")

