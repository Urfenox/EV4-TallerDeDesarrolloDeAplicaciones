import sql_conn



def Agregar(Nombre, num_Area):
    # verificar en que codigo van
    sql_conn.miCursor.execute("SELECT * FROM DEPARTAMENTO;")
    contenido = sql_conn.miCursor.fetchall()
    contadorActual = len(contenido)
    sql_conn.miCursor.execute("INSERT INTO DEPARTAMENTO VALUES (?, ?, ?);", (contadorActual, Nombre, num_Area))
    print("\n Departamento '{}: {}: {}' agregado \n".format(contadorActual, Nombre, num_Area))
    sql_conn.conn.commit()

def Modificar():
    print("No disponible")

def Eliminar():
    print("No disponible")

def Obtener():
    print("No disponible")
