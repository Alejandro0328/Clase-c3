f =None
try:
    f = open("mbox-short.txt")
    print("Se abrio correctamente el archivo")
    # cadena = f.read()
    # print(cadena)
    
    # f.seek(109)
    # linea= f.readline()
    # print(linea)
    
    # for i in range(1,4):
    #     linea= f.readline()
    #     if i == 3:
    #         print(linea)
        
    f.seek(0)# ubica el cursor del archivo al principio
    
    # #leer todo el archivo de principio a fin
    # linea = f.readline()
    # while linea != "":
    #     print(linea.strip())
    #     linea = f.readline()
    
    #*** leer un archivp con readlines()
    lineas = f.readlines()
    print(lineas)
except FileNotFoundError:
    print("Error.No se encontro el archivo.")
except PermissionError:
    print("Error.No se encontro el archivo.")
except Exception as e:
    print(f"Error al abrir el archivo. \n{e}")
finally:
    if f is not None:
        f.close()
        print("Se cerro el archivo correctamente")
