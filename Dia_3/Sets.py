mi_set = set([1,2,3,4,5])
print(mi_set)
#python elimina los objetos repetidos
#no son modificables
#no se pueden poner listas dentro de los sets
#no se pueden navegar los valores
#no admites diccionarios
#SI ADMITE TUPLAS ya que los tuples son inmutables
print(len(mi_set))
print(2 in mi_set)

#Union de sets

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

#Metodo agregar add
s1.add(6)
print(s1)
#Metodo remover remove
s1.remove(6)
print(s1)
#Metodo descartar si no lo encuentra, no tira error
s1.discard(5)
print(s1)
#Metodo pop elimina un elemento aleatorio xD
s1.pop()
print(s1)
#Metodo clear vacia todo el set
s1.clear()
print(s1)