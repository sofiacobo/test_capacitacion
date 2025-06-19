import csv
from modulos.transaccion import Transaccion

class Sistema:
    def __init__(self):
        self.transacciones = []

    def mostrar_menu(self):
        print("\n --- MENÚ DE OPERACIONES ---")
        print("1. Ver transacciones.")
        print("2. Agregar una nueva transacción")
        print("3. Validar transacciones. ")
        print("4. Salir. ")
        print("5. Imoprtar desde CSV")
        print("5. Exportar a CSV")

    def ver_transacciones(self):
        if not self.transacciones:
            print("No hay transacciones registradas")
        else:
            print("Lista de transacciones")
            for t in self.transacciones:
                print(t)
    
    def agregar_transacciones(self):
        try:
            monto = float(input("Ingrese el monto de la transacción: ")) #se ingresa monto
            moneda = input("Ingrese la moneda (ARS/USD): ").upper() #se usa upper para pasar a mayus
            if moneda not in ("ARS", "USD"): #se pasa una tupla para validar
                print("Moneda ingresada incorrecta")
                return #con return no hace falta else? 
            nueva_transaccion = Transaccion(id=len(self.transacciones)+1, monto=monto, moneda=moneda) #se agrega un objeto del tipo transaccion y se pasa los valores
            self.transacciones.append(nueva_transaccion) #se agrega la nueva trx a la lista definida en el init 
            print("Transacción agregada correctamente.")
        except ValueError:
            print("Error: el monto debe ser un número.")

    def validar_transacciones(self):
        if not self.transacciones:
            print("No hay transacciones registradas")
        else:
            print("Validación de transacciones: ")
            for t in self.transacciones: #recorro la lista
                estado = t.validar() #metodo de la clase Transaccion que devuelve un return 
                print(f"{t} -> {estado}")

    def importar_csv(self,ruta):
        try:
            with open(ruta, mode='r', newline="", encoding='utf-8') as archivo: #archivo es un alias
                lector = csv.DictReader(archivo) #al lector le paso el archivo
                for fila in lector:
                    nueva_transaccion = Transaccion(
                        id=int(fila["id"]), #le paso los valores de las columnas del csv
                        monto=float(fila["monto"]), #columna monto del csv
                        moneda=fila["moneda"] #columna moneda del csv
                    )
                    self.transacciones.append(nueva_transaccion)
            print("Transacciones importadas exitosamente.")
        except FileNotFoundError: #excepcion creada para cuando no encuentra un archivo
            print("Archivo no encontrado.")
        except Exception as e:
            print(f"Error al importar archivo: {e}")

    def exportar_csv(self,ruta):
        try:
            with open(ruta, mode='w', newline="", encoding='utf-8') as archivo:
                campos = ["id","monto","moneda"]
                escritor=csv.DictWriter(archivo,fieldnames=campos)
                escritor.writeheader()
                for t in self.transacciones:
                    escritor.writerow(
                        {
                            "id":t.id,
                            "monto":t.monto,
                            "moneda":t.moneda
                        }
                    )
            print("Transacciones exportadas exitosamente!")
        except Exception as e:
            print(f"Error al exportar: {e}")