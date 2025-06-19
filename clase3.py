##CONDICIONALES
## IF and IF ELSE

"""color1 = "blanco"
color2 = "negro"
color3 = "blanco"

if color1 == color2:
    print("Los colores son iguales")
else:
    print("Los colores NO son iguales")

##ELIF
if color1 == color2:
    print("Los colores son iguales")
elif color1 == color3:
    print("Los colores son iguales")
else:
    print("Los colores NO son iguales") """

##PROBLEMA

"""valor_estacionamiento = 1000

print("Bienvenido! Para ingresar al estacionamiento debe abonar el monto de $1000")

monto_ingresado = int(input("Por favor, ingrese el monto: "))

if monto_ingresado == valor_estacionamiento:
    print("La barrera se levantará para que pueda ingresar. Muchas gracias.")
else:
    print("El monto ingresado no es correcto, no puede pasar") """

##SOLUCION 2
"""valor_estacionamiento = 1000

print("Bienvenido! Para ingresar al estacionamiento debe abonar el monto de $1000")

monto_ingresado = int(input("Por favor, ingrese el monto: "))

if monto_ingresado == valor_estacionamiento:
    print("La barrera se levantará para que pueda ingresar. Muchas gracias.")
elif monto_ingresado > valor_estacionamiento:
    vuelto = monto_ingresado - valor_estacionamiento
    print(f"Puede pasar, su vuelto es de ${vuelto}. Muchas gracias")
else:
    print("El monto ingresado no es correcto, no puede pasar")

valor_estacionamiento = 1000

print("Bienvenido! Para ingresar al estacionamiento debe abonar el monto de $1000")

monto_ingresado = int(input("Por favor, ingrese el monto: "))

while(monto_ingresado != valor_estacionamiento):
    print("El monto ingresado no es correcto. El valor es de $1000")
    monto_ingresado = int(input("Por favor, ingrese nuevamente el monto a pagar: "))
print("La barrera se levantará para que pueda ingresar. Muchas gracias.")

clave_correcta = "clave123"
intentos = 3

while (intentos>0):
    clave_ingresada = input("Ingrese su clave: ")
    if clave_ingresada == clave_correcta:
        print("Acceso concedido. Puede ingresar")
        break
    else:
        intentos -=1
        print(f"Clave incorrecta. Intentos restantes: {intentos}")
else:
    print("Acceso bloqueado.")
"""

#while true - break

#bandera = true
#while bandera -> bandera = false

"""for a in range(10):
    print(a) """

transacciones = []
while True:
    print("\n --- MENÚ DE OPERACIONES ---")
    print("1. Ver transacciones.")
    print("2. Agregar una nueva transacción")
    print("3. Validar transacciones. ")
    print("4. Salir. ")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        if not transacciones: 
            print("No hay transacciones registradas")
        else: 
            print("Lista de transacciones: ")
            for t in transacciones:
                print("ID: ", t["id"], "| MONTO: ", t["monto"], "| MONEDA: ", t["moneda"])
    elif opcion == "2":
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
    elif opcion == "3":
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
    elif opcion == "4":
        print("Saliendo del sistema.")
        break
    else:
        print("Opción no válida. Intenta nuevamente. ")