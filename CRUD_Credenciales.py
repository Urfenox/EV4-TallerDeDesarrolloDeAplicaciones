import os
import sql_conn

# Este script se encarga de realiar las operaciones basicas CRUD para la tabla 'Credenciales'

def Agregar(codCredencial, IDENT, Usuario, Clave):
    # Es posible que la Clave se deba generar automaticamente.
    sql_conn.miCursor.execute("INSERT INTO EMPLEADO VALUES (?, ?, ?, ?);", (codCredencial, IDENT, Usuario, Clave))
    print("\n Credencial '{}:{}' creada.\n".format(IDENT, Clave))

def Modificar():
    print("No disponible")

def Eliminar():
    print("No disponible")

def Obtener():
    print("No disponible")