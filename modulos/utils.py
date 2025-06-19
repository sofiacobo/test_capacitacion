#Funcion para mostrar el menú
def mostrar_menu():
    """Retorna con un print las opciones disponibles"""
    print("\n --- MENÚ DE OPERACIONES ---")
    print("1. Ver transacciones.")
    print("2. Agregar una nueva transacción")
    print("3. Validar transacciones. ")
    print("4. Salir. ")

#Funcion para ver transacciones(1)
def ver_transacciones(transacciones):
    """Retorna la lista de transacciones formateada"""
    if not transacciones: 
        print("No hay transacciones registradas")
    else: 
        print("Lista de transacciones: ")
        for t in transacciones:
            print("ID: ", t["id"], "| MONTO: ", t["monto"], "| MONEDA: ", t["moneda"])

def agregar_transacciones(transacciones):
    try:
        monto = float(input("Ingrese el monto de la transacción: "))
        moneda = input("Ingrese la moneda (ARS/USD): ").upper()
        if moneda != "ARS" and moneda != "USD":
            print("Moneda ingresada incorrecta")
        else:
            nueva = {
                "id" : len(transacciones) + 1,
                "monto" : monto,
                "moneda" : moneda
            }
            transacciones.append(nueva)
            print("Transacción agregada con éxito")
    except ValueError:
        print("Error: el monto debe ser un número")

#Función para validar las transacciones
def validar_transacciones(transacciones):
    if not transacciones:
            print("No hay transacciones registradas")
            for t in transacciones:
                if t["monto"] <= 0:
                    estado = "Monto inválido"
                elif t["moneda"] == "ARS" and t["moneda"] > 100000:
                    estado = "Requiere una autorización adicional"
                elif t["moneda"] == "USD" and t["moneda"] > 10000:
                    estado = "Requiere una autorización adicional por monto en divisa USD"
                else:
                    estado = "Transaccion válida!"
                print(f"ID: {t["id"]}, : {estado}")