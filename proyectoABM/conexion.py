import mysql.connector
from mysql.connector import Error

# Genera la conexion con el BD
class Conexion:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host="localhost",         # Cambia si usás otro servidor
                user="root",              # Tu usuario en MariaDB
                password="1111",              # Tu contraseña (si tenés)
                database="proyectoABM"    # Asegúrate de que esta base exista
            )
            self.cursor = self.conexion.cursor()
            print("✅ Conexión exitosa a la base de datos.")
        except Error as err:
            print(f"❌ Error al conectar: {err}")
            self.conexion = None
            self.cursor = None
            
# Cierra la conexion con la BD
    
    def cerrar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()
            print("🔒 Conexión cerrada.")


