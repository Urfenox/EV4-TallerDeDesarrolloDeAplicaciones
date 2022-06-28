from asyncio.windows_events import NULL
import sql_conn

strPluralMin = "Areas"
strSingularMin = "Area"
strNombreTabla = "AREA"

def Agregar(Nombre):
    # verificar en que codigo van
    sql_conn.miCursor.execute("SELECT * FROM ?;", (strNombreTabla))
    contenido = sql_conn.miCursor.fetchall()
    contadorActual = len(contenido)
    sql_conn.miCursor.execute("INSERT INTO ? VALUES (?, ?);", (strNombreTabla, contadorActual, Nombre))
    print("\n {} '{}: {}' agregada \n".format(strSingularMin, contadorActual, Nombre))
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
            print("\n    Codigo: {}\n    Nombre: {}\n".format(item[0],item[1]))
        print("--- Fin registros '{}' ---".format(strSingularMin))
    else:
        # Opcion 2: Buscar y mostrar
        sql_conn.miCursor.execute("SELECT * FROM ? WHERE codArea=?;", (strNombreTabla, PK))
        items = sql_conn.miCursor.fetchall()
        for item in items:
            print("\n    Codigo: {}\n    Nombre: {}\n".format(item[0], item[1]))

# SOLO PARA PRUEBAS
# # Crear conexion
# sql_conn.abrirConn()
# # Iniciar Base de Datos
# sql_conn.iniciarDB()
# #   Agregar
# continuar = True
# while continuar:
#     print("¿Ingresar Area?\n    1. Si\n    2. No")
#     op = int(input("Ingrese la opcion: "))
#     if (op == 2):
#         continuar = False
#         break
#     Agregar(input("Ingrese el nombre del 'Area': "))

# #   Obtener
# continuar = True
# while continuar:
#     print("¿Obtener 'Area'?\n    1. Si\n    2. No")
#     op = int(input("Ingrese la opcion: "))
#     if (op == 2):
#         continuar = False
#         break
#     PK = input("Ingrese la PK del 'Area': ")
#     if (PK == ""):
#         Obtener()
#     else:
#         Obtener(PK)
