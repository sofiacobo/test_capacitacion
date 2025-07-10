import mysql.connector
from dotenv import load_dotenv
import os 

load_dotenv()

#se abre la conexion a la bd y se llaman a las variables de entorno
conn = mysql.connector.connect(
    host = os.getenv("DB_HOST"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASS"),
    name = os.getenv("DB_HNAME")
)