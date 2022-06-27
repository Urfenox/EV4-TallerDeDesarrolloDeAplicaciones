import sql_conn



def Agregar(Nombre):
    # verificar en que codigo van
    sql_conn.miCursor.execute("SELECT * FROM RELACION;")
    contadorActual = (len(sql_conn.miCursor.fetchall()) + 1)
    sql_conn.miCursor.execute("INSERT INTO RELACION VALUES (?, ?);", (contadorActual, Nombre))
    print("\n Relacion '{}: {}' agregada \n".format(Nombre, contadorActual))

def Modificar():
    print("No disponible")

def Eliminar():
    print("No disponible")

def Obtener():
    print("No disponible")
