import json
cliente ={}
def registro_cliente():
    print("Regsitro Cliente")
    print("Primero debe regsitrar los siguientes datos para poder ordenar un gas a domicilio")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    direccion = ("Direccion: ")
    sector = input("Sector: ")
    if sector.lower() == "centro" or "Colina" or "Industrias":
            gas=input("Ingrese el gas a comprar entre las siguientes opciones\n1. Cil. 5kg\n2. Cil. 15kg\n3. Cil.45kg\n")
            cantidad= int(input("Ingresese cuantos gas quiere: "))
            confirmar = input("¿Desea confirmar su pedido? (si/no): ")
            if confirmar.lower() == "si":
                cliente[sector] = {
                    "nombre": nombre,
                    "apellido": apellido,
                    "sector": sector,
                    "direccion": direccion,
                    "gas": gas,
                    "cantidad":cantidad
                    }
            else:
                return menu()
    else:
        print("No realizamos pedidos a ese sector")
def listar_pedidos(): 
     print(cliente)
def imprimir_hoja():
    if "sector" in cliente!=None:
        with open('HojaRuta.json','w') as archivo:
            json.dump(cliente, archivo)
    else:
        print("No se han registrado datos")
        return menu()
def salir():
    breakpoint
def menu():
    while True:
        print("Bienvenido a Gaxplosive")
        print("1. Registrar pedidos")
        print("2. Listar todos los pedidos")
        print("3. Imprimir hoja de ruta")
        print("4. Salir")
        try:
            opcion = int(input("Ir a: "))
        except ValueError:
            print("Opcion no válida. Debe ingresar una opcion valida entre 1 y 5.")
        if opcion == 1:
            registro_cliente()
        elif opcion == 2:
            listar_pedidos()
        elif opcion == 3:
            imprimir_hoja()
        elif opcion == 4:
            salir()
            break
menu()
with open('HojaRuta.json','w') as archivo:
    json.dump(cliente, archivo)