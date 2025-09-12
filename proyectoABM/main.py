import tkinter as tk
from tkinter import ttk, messagebox
from modelos.contactos import (
    crear_tabla_contactos,
    insertar_contacto,
    listar_contactos,
    eliminar_contacto,
    modificar_contacto
)

# Crear tabla al iniciar
crear_tabla_contactos()

# Ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Contactos")
ventana.geometry("700x400")

# Campos de entrada
tk.Label(ventana, text="Nombre").grid(row=0, column=0, padx=5, pady=5)
nombre_entry = tk.Entry(ventana)
nombre_entry.grid(row=0, column=1, padx=5)

tk.Label(ventana, text="Correo").grid(row=1, column=0, padx=5, pady=5)
correo_entry = tk.Entry(ventana)
correo_entry.grid(row=1, column=1, padx=5)

tk.Label(ventana, text="Teléfono").grid(row=2, column=0, padx=5, pady=5)
telefono_entry = tk.Entry(ventana)
telefono_entry.grid(row=2, column=1, padx=5)

# Tabla de contactos con Treeview
tabla = ttk.Treeview(ventana, columns=("ID", "Nombre", "Correo", "Teléfono"), show="headings")
tabla.grid(row=4, column=0, columnspan=4, pady=10)

for col in ("ID", "Nombre", "Correo", "Teléfono"):
    tabla.heading(col, text=col)

# Funciones
def actualizar_tabla():
    for fila in tabla.get_children():
        tabla.delete(fila)
    contactos = listar_contactos()
    for contacto in contactos:   # ahora contactos es lista, no None
        tabla.insert("", "end", values=contacto)

def agregar_contacto():
    nombre = nombre_entry.get()
    correo = correo_entry.get()
    telefono = telefono_entry.get()
    if nombre:
        insertar_contacto(nombre, correo, telefono)
        actualizar_tabla()
        nombre_entry.delete(0, tk.END)
        correo_entry.delete(0, tk.END)
        telefono_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Campo vacío", "El nombre es obligatorio.")

def eliminar_seleccionado():
    seleccionado = tabla.selection()
    if seleccionado:
        valores = tabla.item(seleccionado)["values"]
        id_contacto = valores[0]
        eliminar_contacto(id_contacto)
        actualizar_tabla()
    else:
        messagebox.showwarning("Sin selección", "Selecciona un contacto para eliminar.")

def modificar_seleccionado():
    seleccionado = tabla.selection()
    if seleccionado:
        valores = tabla.item(seleccionado)["values"]
        id_contacto = valores[0]
        nombre = nombre_entry.get()
        correo = correo_entry.get()
        telefono = telefono_entry.get()
        if nombre:
            modificar_contacto(id_contacto, nombre, correo, telefono)
            actualizar_tabla()
        else:
            messagebox.showwarning("Campo vacío", "El nombre es obligatorio.")
    else:
        messagebox.showwarning("Sin selección", "Selecciona un contacto para modificar.")

# Botones
tk.Button(ventana, text="Agregar", command=agregar_contacto).grid(row=3, column=0, pady=5)
tk.Button(ventana, text="Eliminar", command=eliminar_seleccionado).grid(row=3, column=1, pady=5)
tk.Button(ventana, text="Modificar", command=modificar_seleccionado).grid(row=3, column=2, pady=5)

# Mostrar contactos al iniciar
actualizar_tabla()

ventana.mainloop()

