import sql_conn



def Agregar(Nombre):
    # verificar en que codigo van
    sql_conn.miCursor.execute("SELECT * FROM AREA;")
    contadorActual = (len(sql_conn.miCursor.fetchall()) + 1)
    sql_conn.miCursor.execute("INSERT INTO AREA VALUES (?, ?);", (contadorActual, Nombre))
    print("\n Area '{}: {}' agregada \n".format(Nombre, contadorActual))

def Modificar():
    print("No disponible")

def Eliminar():
    print("No disponible")

def Obtener():
    print("No disponible")
