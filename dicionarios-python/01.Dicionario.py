# diccionario vacio
dicc ={}
dicc= dict()
#asignar valores
camper = {
    "nombre": "Sebastian",
    "Edad":"18",
    "carrera":"Ingeniera de sistemas"}

producto = dict(nombre ="Portatil", precio=4000_000,stok=10)

# creacion con lista de tuplas
pares = [("a",1), ("b",2),("c",3)]
diccionaario = dict(pares)

#acceso
print(camper["nombre"])
print(camper.get("edad"))
print(camper.get("pasatiempos","ping pong"))
# metodo keys(): devuelve uan lista con todas las llaves
print(camper.keys())
camper["pasatiempos"] = "futbol"

#metodo values():devuelve todos los valores
print(camper.values()
)
# metodo items():devuelve todos lso pares clave -valor como una lista de tuplas
print(camper.items())

#recorrer
#1. con keys()
for key in camper.keys():
    print(f"campers [{key}]->{camper[key]}", end=", ")


# 2. con items()

for llave,valor in camper.items():
    print(f"campers [{llave}]->{valor}", end=", ")

# pop(): elimina una clave y retorna su valor
print(camper.pop("pasatiempos"))
print(camper)


#popitem(): elimina y retorna el ultimo par clave-valor insertado
print(camper.popitem())
print(camper)

#clear():elimina todos los elementos del diccionario
#camper.clear()
# camper = {}

#copy() : crea una copia del diccionario
camper_bak={}
camper_bak= camper.copy()
print (camper_bak)

# setdefaul(): retorna el valor de una clave. Sino existe , la crea con un valor por defecto.

print(camper.setdefault("pasatiempo", ["futbol","Programar","parandear"]))
print(camper)
print(camper.setdefault("pasatiempo", "dormir"))

# len(): cantidad de pares -valor que hay en el diccionario
print (len(camper))

#in : verifica si existe una llave en el diccionario
print("sexo" in camper)

#del: elimina una llave
del camper["pasatiempos"]
# any(): verifica si al menos un valor de las llaves verdadero
camper["sueldo"] = 0
print(camper)
print(any(camper.values()))

# all():verifica si al todos lo valores d elas llaves son verdaderos
print(all(camper.values())) # -> False