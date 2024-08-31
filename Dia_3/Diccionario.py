diccionario = {"nombre": ["Francisco", "Luis"],"apellido": "Quarñolo","edad":26,"peso":80,"altura":1.74}
#print(diccionario)

#print(diccionario["nombre"][0])

dic = {"c1":["a","b","c"], "c2":["d","e","f"]}
#print(dic["c2"][1].upper())

dic2 = {1:"a",2:"b"}
#print(dic2)

#añado una variable
dic2[3] = "c"
#print(dic2)

#sobreescribo un valor que ya existe en un dic
dic2[2] = "B"
#print(dic2)

#conocer todas las claves que hay en un dic
#print(dic.keys()) #claves
#print(dic.values()) #valores
#print(dic.items()) #items

#mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
#print(mi_dict["puntos"]["points2"][1])

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic["edad"]=36
mi_dic["ocupacion"]="Editora"
mi_dic["pais"]="Colombia"
print(mi_dic)