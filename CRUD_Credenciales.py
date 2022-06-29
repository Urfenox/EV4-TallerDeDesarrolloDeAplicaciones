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

def Modificar(codCredencial, Nombre, Clave):
    sql_conn.miCursor.execute("UPDATE ? SET Usuario=?, Clave=? WHERE codCredencial=?;", (strNombreTabla, Nombre, Clave, codCredencial))
    print("\n {} '{}: {}: {}' modificada \n".format(strSingularMin, codCredencial, Nombre, Clave))

def Eliminar(codCredencial):
    sql_conn.miCursor.execute("DELETE FROM ? WHERE codCredencial=?;", (strNombreTabla, codCredencial)) 
    print("\n {} '{}' eliminada \n".format(strSingularMin, codCredencial))

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

# Controladores
#   C = Crear()
#   R = Explorar()
#   U = Actualizar()
#   D = Remover

def Crear(): # Agrega un registro. Pide los datos
    Agregar(int(input("Ingrese el vinculo IDENT: ")), input("Ingrese el Usuario: "), input("Ingrese la Clave: "))

def Explorar(): # Obtener un registro. Pide PK
    print("Hay dos Opciones para esta funcion:\n    1. Listar todos\n    2. Buscar uno")
    op = int(input("Ingrese la opcion: "))
    if (op == 1):
        Obtener()
    elif (op == 2):
        Obtener(int(input("Ingrese el Codigo de la Credencial: ")))
    else:
        print("Opcion no valida")

def Actualizar(): # Modificar un registro. Pide PK y nuevos datos
    codCredencial = int(input("Ingrese el Codigo del Credencial: "))
    # Obtener (listar y mostrar)
    Obtener(codCredencial)
    Usuario = input("Ingrese el nuevo nombre de usuario: ")
    Clave = input("Ingrese la nueva Clave: ")
    Modificar(codCredencial, Usuario, Clave)

def Remover(): # Eliminar un registro. Pide PK
    Eliminar(int(input("Ingrese el Codigo de la Credencial: ")))
