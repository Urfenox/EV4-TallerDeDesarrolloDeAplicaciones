import sql_conn



def Agregar(Nombre, num_Departamento):
    # verificar en que codigo van
    sql_conn.miCursor.execute("SELECT * FROM CARGO;")
    contadorActual = (len(sql_conn.miCursor.fetchall()) + 1)
    sql_conn.miCursor.execute("INSERT INTO CARGO VALUES (?, ?);", (contadorActual, Nombre))
    print("\n Cargo '{}: {}' agregado \n".format(Nombre, contadorActual))

def Modificar():
    print("No disponible")

def Eliminar():
    print("No disponible")

def Obtener():
    print("No disponible")
