import sql_conn
import Utilidades



def Agregar(Nombre):
    # verificar en que codigo van
    sql_conn.miCursor.execute("SELECT * FROM SEXO;")
    contenido = sql_conn.miCursor.fetchall()
    contadorActual = len(contenido)
    sql_conn.miCursor.execute("INSERT INTO SEXO VALUES (?, ?);", (contadorActual, Nombre))
    print("\n Sexo '{}: {}' agregado \n".format(Nombre, contadorActual))
    sql_conn.conn.commit()

def Modificar():
    print("No disponible")

def Eliminar():
    print("No disponible")

def Obtener():
    print("No disponible")
