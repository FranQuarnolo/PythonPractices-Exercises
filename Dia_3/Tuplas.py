mi_tuple = (1,2,(10,20),4)

t= (1,2,3)
x,y,z=t
#tiene la misma cantidad de valores entonces se asingan correspondientemente
print(x,y,z)
print(mi_tuple[2])

t= (1,2,3,1)
#cuenta los elementos que aparecen dentro de la tupla
print(t.count(1))

#me da el indice de donde se encuetra un valor x
print(t.index(2))


