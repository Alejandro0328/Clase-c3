import json
campers = {
        "Julian" :[10, 20 , 30, 40, 60],
        "Michelle": [50,40,30,50],
        "Jesus" : [30, 30, 40, 30]

    
         
}

with open ("lista.json", "w") as archivo:
    json.dump(campers, archivo)# descarga la lista en el archivo formato jdon
    print("Datos guardados")