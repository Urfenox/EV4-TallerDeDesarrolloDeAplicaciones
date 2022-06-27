import sql_conn



def Agregar(Nombre, num_Area):
    # verificar en que codigo van
    sql_conn.miCursor.execute("SELECT * FROM DEPARTAMENTO;")
    contadorActual = (len(sql_conn.miCursor.fetchall()) + 1)
    sql_conn.miCursor.execute("INSERT INTO DEPARTAMENTO VALUES (?, ?);", (contadorActual, Nombre))
    print("\n Departamento '{}: {}' agregado \n".format(Nombre, contadorActual))

def Modificar():
    print("No disponible")

def Eliminar():
    print("No disponible")

def Obtener():
    print("No disponible")
