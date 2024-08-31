mi_lista = ["a","b","c"]
mi_lista2 = ["d","e","f"]
print(mi_lista)
print(len(mi_lista))
print(mi_lista[::-1])

mis_listas = mi_lista+mi_lista2
print(mis_listas)

mis_listas[0] = "alfa"
print(mis_listas)

mis_listas.append("g")
print(mis_listas)

mis_listas.pop()
print(mis_listas)

eliminado= mis_listas.pop(0)
print(mis_listas, eliminado)

mis_listas.sort()
print(mis_listas)

mis_listas.reverse()
print(mis_listas)




