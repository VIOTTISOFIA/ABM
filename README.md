En el marco de la Tecnicatura en analisis de datos e I.A. realizada en el ISCP de la cohorte 2025, el equipo de trabajo,
integrado por: Katya Nadales, Sofía Viotti, Luca Zunino. y Lucas Gonella. Realizo el siguiente proyecto en el marco del modulo de PROGRAMACION I.

Esta es  aplicación de escritorio desarrollada en Python utilizando la librería Tkinter para la interfaz gráfica.
Su propósito es gestionar una base de datos de contactos, permitiendo a los usuarios funciones de manipulacion de datos (DML) :
crear,ver, modificar y eliminar información de contacto.

Características Principales
 * Interfaz Gráfica (GUI): Construida con Tkinter, cuya presentaciopn al usuario final la hace accesible e intuitiva.
 * Gestión de Datos: Permite agregar nuevos contactos, visualizar todos los contactos en una tabla, modificar la información existente y eliminar registros.
 * Base de Datos Simple: Utiliza un sistema de base de datos ligero para almacenar la información de los contactos de forma persistente.
 * 
Requisitos
Para ejecutar esta aplicación, necesitas tener instalado Python 3. Las librerías necesarias son:
 * Tkinter: Generalmente viene incluida con la instalación estándar de Python.
 * Módulo de base de datos: El código hace referencia a un módulo modelos.contactos, que probablemente maneja la conexión y
 * las operaciones con una base de datos como SQLite. Asegúrate de tener este archivo y el módulo de base de datos correspondiente (por ejemplo, sqlite3) en tu entorno.
 * 
Cómo Ejecutar la Aplicación
 * Asegúrate de tener el archivo principal (main.py o similar) y el módulo modelos/contactos.py en la misma carpeta.
 * Abre una terminal o línea de comandos.
 * Navega hasta el directorio donde se encuentran los archivos.
 * Ejecuta el siguiente comando:
<!-- end list -->
python3 main.py

Uso
 * Agregar un contacto: Introduce el nombre, correo y teléfono en los campos de texto y haz clic en el botón "Agregar".
 * Ver contactos: Los contactos se mostrarán automáticamente en la tabla principal.
 * Eliminar un contacto: Selecciona una fila en la tabla y haz clic en el botón "Eliminar".
