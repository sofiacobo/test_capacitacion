# from datetime import datetime, timedelta

# ahora = datetime.now() #trae la fecha de hoy en ese preciso momento
# print(f"Ahora: {ahora}")
# print(f"Mañana: {ahora + timedelta(days=1)}")

# import random 

# print(random.randint(1,100)) #genera un numero random
# print(random.choice(["piedra", "papel","tijera"])) #imprime algo aleatorio de una lista

# import math
# print(math.pi)
# print(math.sqrt(16))

# import os

# print("Archivos: ", os.listdir()) #lista todos los archiovs y carpetas

# from collections import Counter

# frutas = ["Manzana", "Banana", "Manzana"]
# print(Counter(frutas)) #cuenta la cantidad de cada fruta que hay en la lista

# import json #para trabajar con apis

# persona = {'nombre' : "Juan", "edad" : 30}
# print(persona)
# json_str = json.dumps(persona) #pasa un diccionario a json
# print(json_str)

### PARA VALIDAR MAILS
# import re

# texto = "Mi email es example@example.com"
# print(re.findall(r'\S+@\S+', texto)) #lo que esta dps de r es un patron que se tiene que buscar en la frase 'texto' -> DEVUELVE UNA LISTA

# import pandas as pd

# data = {"Nombre": ["Juan", "Jose", "Ana"], "Edad" : [30,25,35]}

# df = pd.DataFrame(data) #se crea un objeto del tipo dataframe
# print(df)

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
USUARIO = os.getenv("USUARIO")
PASSWORD = os.getenv("PASSWORD")