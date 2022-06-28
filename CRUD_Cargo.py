from asyncio.windows_events import NULL
import sql_conn

strPluralMin = "Cargos"
strSingularMin = "Cargo"
strNombreTabla = "CARGO"

def Agregar(Nombre, num_Departamento):
    # verificar en que codigo van
    sql_conn.miCursor.execute("SELECT * FROM ?;", (strNombreTabla))
    contenido = sql_conn.miCursor.fetchall()
    contadorActual = len(contenido)
    sql_conn.miCursor.execute("INSERT INTO ? VALUES (?, ?, ?);", (strNombreTabla, contadorActual, Nombre, num_Departamento))
    print("\n {} '{}: {}: {}' agregado \n".format(strSingularMin, Nombre, contadorActual, num_Departamento))
    sql_conn.conn.commit()

def Modificar():
    print("No disponible")

def Eliminar():
    print("No disponible")

def Obtener(PK=NULL):
    # Obtener lista todos los datos
    #   Opciones:
    #       Obtener(sinParametro): Lista todos los registros
    #       Obtener(Parametro=PK): Muestra el registro coincidente con la PK.
    if (PK == NULL):
        # Opcion 1: Buscar y mostrar todos
        sql_conn.miCursor.execute("SELECT * FROM ?;", (strNombreTabla))
        items = sql_conn.miCursor.fetchall()
        print("--- Inicio registros '{}' ---".format(strSingularMin))
        for item in items:
            print("\n    Codigo: {}\n    Nombre: {}\n    Departamento: {}\n".format(item[0], item[1], item[2]))
        print("--- Fin registros '{}' ---".format(strSingularMin))
    else:
        # Opcion 2: Buscar y mostrar
        sql_conn.miCursor.execute("SELECT * FROM ? WHERE codDepartamento=?;", (strNombreTabla, PK))
        items = sql_conn.miCursor.fetchall()
        for item in items:
            print("\n    Codigo: {}\n    Nombre: {}\n    Departamento: {}\n".format(item[0], item[1], item[2]))
