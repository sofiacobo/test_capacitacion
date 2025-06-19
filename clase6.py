## HERENCIA

class Vehiculo:

    def __init__(self, ruedas, marca, modelo, color):
        self.ruedas = ruedas
        self.marca = marca
        self.modelo = modelo
        self.color = color 

    # Método de instancia acelerar
    def acelerar(self): #self hace referencia al objeto
        print(f"El {self.marca} {self.modelo} está acelerando")  
    
class Coche(Vehiculo):
    pass

class Bicicleta(Vehiculo):
    pass

coche_1 = Coche(4, "Renault", "Sandero", "Negro")
bici_1 = Coche(2, "SLP", "100pro", "Negro")

class A:
    def __init__(self):
        print("Soy la clase A")

class B:
    def __init__(self):
        print("Soy la clase B")

class C(A,B):
    def __init__(self):
        super()
        print("Soy la clase C")