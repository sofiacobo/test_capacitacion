# from modulos import transaccion
# from modulos.sistema import Sistema

# sistema = Sistema()

# while True:
#     sistema.mostrar_menu()
#     opcion = input("Seleccione una opción (1-6): ")

#     if opcion == "1":
#         sistema.ver_transacciones()
#     elif opcion == "2":
#         sistema.agregar_transacciones()
#     elif opcion == "3":
#         sistema.validar_transacciones()
#     elif opcion == "4":
#         print("Saliendo del sistema.")
#         break
#     elif opcion == "5":
#         ruta=input("Ingrese la ruta del archivo csv: ")
#         sistema.importar_csv(ruta)
#     elif opcion=="6":
#         ruta=input("Ingrese una truta donde guardar el CSV: ")
#         sistema.exportar_csv(ruta)
#     else:
#         print("Opción no válida. Intenta nuevamente. ")

class Prestamo:
    def __init__(self, capital, tasa, cuota):
        self.capital = capital
        self.tasa = tasa
        self.cuota = cuota

    def calculo_cuota(capital, tasa, cuota):
        valor_cuota = capital * (tasa * (1 + tasa) ** cuota) / ((1 + tasa) ** cuota - 1)
        return valor_cuota

prestamo_1 = Prestamo(10000, 60, 12)
print(prestamo_1.calculo_cuota)