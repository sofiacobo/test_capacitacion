## POO

class Coche: 
    
    ruedas = 4 #atributo de clase que comparten todas las instancias de la clase

    # Constructor
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    #se usa cuando se llama al objeto
    def __str__(self):
        return f"Coche {self.marca}, {self.modelo} de color {self.color}"

    # Método de instancia acelerar
    def acelerar(self): #self hace referencia al objeto
        print(f"El {self.marca} {self.modelo} está acelerando")

    # Método de clase incrementar ruedas
    @classmethod #esto es un decorador -> es una funcion que utiliza adentro otra funcion que se pasa como parametro
    def incrementar_ruedas(cls): #cls es un argumento que representa a la CLASE
        cls.ruedas += 1
    
    # Método estático
    # no usa variable definidas en la clase y no dependen de la clase
    # pero el uso que se le da esta relacionado a la clase, se definen dentro de la misma
    @staticmethod
    def calcular_distancia(velocidad, tiempo):
        return velocidad * tiempo

# Creamos objetos a partir de una clase
coche_1 = Coche("Toyota", "Corolla", "Rojo")
coche_2 = Coche("Peugeot", "308", "Azul")

# Acceder al estado de los atributos que definimos anteriormente
print("Primer coche: ")
print(coche_1.marca) #con el punto se accede a un atributo particular que definimos del objeto
print(coche_1.modelo)
print(coche_1.color)


#Llamo al metodo acelerar y uso el coche 1
coche_1.acelerar()

Coche.incrementar_ruedas()
print(f"El coche {coche_1.marca} {coche_1.modelo} tiene {coche_1.ruedas} ruedas")

print(f"El {coche_1.modelo} va a {coche_1.calcular_distancia(60,2)} km/h")

