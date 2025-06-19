#PROGRAMACION FUNCIONAL

def sumar(x,y):
    """retorna el resultado de la suma de dos numeros"""
    resultado = x + y
    return resultado

#print(sumar(4,5))

def saludar_con_valor_por_def(nombre, mensaje="Hola"):
    return f"{mensaje}, {nombre}"

#print(saludar_con_valor_por_def("Sofía"))

def suma(**kwargs):
    resultado = 0
    for clave, valor in kwargs.items():
        print(clave, "=", valor)
        resultado += valor

    return resultado

def operaciones(x,y):
    suma = x + y
    resta = x - y
    return suma, resta

variable_1, variable_2 = operaciones(5,4)

#print(variable_1)
#print(variable_2)