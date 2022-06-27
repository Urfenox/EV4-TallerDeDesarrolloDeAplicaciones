import sql_conn



def Agregar(Nombre, num_Departamento):
    # verificar en que codigo van
    sql_conn.miCursor.execute("SELECT * FROM CARGO;")
    contenido = sql_conn.miCursor.fetchall()
    contadorActual = len(contenido)
    sql_conn.miCursor.execute("INSERT INTO CARGO VALUES (?, ?, ?);", (contadorActual, Nombre, num_Departamento))
    print("\n Cargo '{}: {}: {}' agregado \n".format(Nombre, contadorActual, num_Departamento))
    sql_conn.conn.commit()

def Modificar():
    print("No disponible")

def Eliminar():
    print("No disponible")

def Obtener():
    print("No disponible")
