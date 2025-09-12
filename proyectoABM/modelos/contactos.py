import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexion import Conexion

def crear_tabla_contactos():
    db = Conexion()
    cursor = db.cursor

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contactos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(50) NOT NULL,
            correo VARCHAR(100),
            telefono VARCHAR(20)
        )
    """)

    db.conexion.commit()
    db.cerrar()
    print("✅ Tabla 'contactos' creada correctamente.")


def insertar_contacto(nombre, correo, telefono):
    db = Conexion()
    cursor = db.cursor

    sql = "INSERT INTO contactos (nombre, correo, telefono) VALUES (%s, %s, %s)"
    valores = (nombre, correo, telefono)
    cursor.execute(sql, valores)

    db.conexion.commit()
    db.cerrar()
    print(f"🟢 Contacto '{nombre}' insertado correctamente.")

    

def listar_contactos():
    db = Conexion()
    cursor = db.cursor

    cursor.execute("SELECT * FROM contactos")
    resultados = cursor.fetchall()

    db.cerrar()
    print("📋 Lista de contactos:")
    for fila in resultados:
        print(f"ID: {fila[0]}, Nombre: {fila[1]}, Correo: {fila[2]}, Teléfono: {fila[3]}")

    return resultados






def eliminar_contacto(id):
    db = Conexion()
    cursor = db.cursor

    cursor.execute("DELETE FROM contactos WHERE id = %s", (id,))
    db.conexion.commit()
    db.cerrar()
    print(f"🗑️ Contacto con ID {id} eliminado.")

def modificar_contacto(id, nombre, correo, telefono):
    db = Conexion()
    cursor = db.cursor

    sql = """
        UPDATE contactos
        SET nombre = %s, correo = %s, telefono = %s
        WHERE id = %s
    """
    valores = (nombre, correo, telefono, id)
    cursor.execute(sql, valores)

    db.conexion.commit()
    db.cerrar()
    print(f"✏️ Contacto con ID {id} modificado.")

