import os
import sql_conn



def Agregar(IDENT, Usuario, Clave):
    # verificar en que codigo van
    sql_conn.miCursor.execute("SELECT * FROM CREDENCIAL;")
    contenido = sql_conn.miCursor.fetchall()
    contadorActual = len(contenido)
    sql_conn.miCursor.execute("INSERT INTO CREDENCIAL VALUES (?, ?, ?, ?);", (contadorActual, IDENT, Usuario, Clave))
    print("\n Credencial '{}: {}: {}' agregada \n".format(contadorActual, IDENT, Usuario))
    sql_conn.conn.commit()

def Modificar():
    print("No disponible")

def Eliminar():
    print("No disponible")

def Obtener():
    print("No disponible")
