"""
Contruya un programa en python para gestiona run inventario de una ferreteria usando diciionarios
"""



def menu():
    print("""*** INVENTARI DERRETERIA EL TORNILLO***
1. Agregar producto
2. Consutar producto
3. Actulizar produto
4: Eliminar producto
5. Buscar producto
6. Productos con bajo stok
7. Valor total del inventario
8. Consultar todos los productos
9. Salir
""")
def cargar_datos(dic_inv):
    dic_inv={
        "MART001":{
            "nombre": "Martillo de uña",
            "precio": 15000,
            "stock":25,
            "categoria":"heramientas"
        },
        "DEST002": {
            "nombre":"Destornillador plano",
            "precio": 8000,
            "stock": 40,
            "categoria":"heramienta"
        },
        "TALA003":{
            "nombre":"Taladro elèctrico",
            "precio": 12000,
            "stock": 8,
            "categoria":"heramienta electrica"
        }
    }
    return dic_inv
def agragar_prd(dinv):
    print("\n\n1. Agregar Producto\n\n")
    cod = input("Còdigo del producto : ").upper()
    #verificar que ya no exista en el dicionario
    if cod in dinv:
        print(f"Error . el producto còdigo { cod} ya existe. ")
        return dinv
    nombre =input ("Nombre: ")
    precio = int (input("Precio: "))
    stock = int (input("Stock: "))
    categoria= input("Categoria: ")
    dinv[cod]= {
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "categoria":categoria
    }
    return dinv

def consultar_todos(dinv):
    print ("\n\n8. Consultar todos los productos\n\n")
    if not dinv:
        print("El inventario esta vacio.")
        return
    print(f"{'Codigo':<10}{'Nombre':<30}{'Precio':<15}{'Stock':<10}{'Categoria':<20}")
    print("-"* 90)

    for cod ,prd in dinv.items():
        print(f"{cod:<10}{prd['nombre']:<30}${prd['precio']:<15}{prd['stock']:<10}{prd['categoria']:<20}")
    print (f"\n Total de productos: {len(dinv)}\n\n\n")


def consultar_prd(dinv):
    print("\n\n2. Consultar Producto\n\n")
    cod= input("Ingrese el código a buscar: ").strip().upper()
    if cod in dinv:
        p = dinv[cod]
        print(f"Nombre: {p['nombre']}")
        print(f"Precio: $ {p['precio']}")
        print(f"Stock: {p['stock']} Unidades")
    else:
        print("Ese producto no esta en el sistema")

def eliminar_producto(dinv):
    print("")
    cod=input("Código del producto a eliminar: ").upper()
    if cod not in dinv:
        print("Este producto no existe......")
        return dinv






def main():
    inventario= {}
    inventario=cargar_datos(inventario)
    # print(inventario)
    while (True):
        menu()
        op = input ("Opcion? ").strip()
        if op == "1":
            inventario= agragar_prd(inventario)
        elif op == "2":
            consultar_prd(inventario)
        elif op == "3":
            pass
        elif op == "4":
            pass
        elif op == "6":
            pass
        elif op == "7":
            pass
        elif op == "8":
            consultar_todos(inventario)
        elif op == "9":
            print("Gracias por usar el programa")
            break
        else:
            print("Opcion no valida: Ingrese un nùmero del 1 - 9")
            input("Ingese cualquier letra para continuar...........")
main()