from asyncio.windows_events import NULL
import sql_conn

strPluralMin = "Credenciales"
strSingularMin = "Credencial"
strNombreTabla = "CREDENCIAL"

def Agregar(IDENT, Usuario, Clave):
    # verificar en que codigo van
    sql_conn.miCursor.execute("SELECT * FROM ?;", (strNombreTabla))
    contenido = sql_conn.miCursor.fetchall()
    contadorActual = len(contenido)
    sql_conn.miCursor.execute("INSERT INTO ? VALUES (?, ?, ?, ?);", (strNombreTabla, contadorActual, IDENT, Usuario, Clave))
    print("\n {} '{}: {}: {}' agregada \n".format(strSingularMin, contadorActual, IDENT, Usuario))
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
            print("\n    Codigo: {}\n    IDENT: {}\n    Usuario: {}\n    Clave: {}\n".format(item[0], item[1], item[2], item[3]))
        print("--- Fin registros '{}' ---".format(strSingularMin))
    else:
        # Opcion 2: Buscar y mostrar
        sql_conn.miCursor.execute("SELECT * FROM ? WHERE codCredencial=?;", (strNombreTabla, PK))
        items = sql_conn.miCursor.fetchall()
        for item in items:
            print("\n    Codigo: {}\n    IDENT: {}\n    Usuario: {}\n    Clave: {}\n".format(item[0], item[1], item[2], item[3]))
