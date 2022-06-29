from asyncio.windows_events import NULL
import sql_conn
import CRUD_Empleados
import CRUD_Relacion
import CRUD_Sexo

strPluralMin = "Cargas Camiliares"
strSingularMin = "Carga Familiar"
strNombreTabla = "CARGA_FAMILIAR"

def Agregar(rut_carga, NombresApellidos, num_Empleado, num_Relacion, num_Sexo):
    # verificar en que codigo van
    sql_conn.miCursor.execute("SELECT * FROM ?;", (strNombreTabla))
    contenido = sql_conn.miCursor.fetchall()
    contadorActual = len(contenido)
    sql_conn.miCursor.execute("INSERT INTO ? VALUES (?, ?, ?, ?, ?);", (strNombreTabla, rut_carga, NombresApellidos, num_Empleado, num_Relacion, num_Sexo))
    print("\n {} '{}: {}: {}' agregada \n".format(strSingularMin, rut_carga, NombresApellidos, num_Empleado))
    sql_conn.conn.commit()

def Modificar(rut_carga, Nombre):
    sql_conn.miCursor.execute("UPDATE ? SET NombresApellidos=? WHERE rut_carga=?;", (strNombreTabla, Nombre, rut_carga))
    print("\n {} '{}: {}' modificado \n".format(strSingularMin, rut_carga, Nombre))

def Eliminar(rut_carga):
    sql_conn.miCursor.execute("DELETE FROM ? WHERE rut_carga=?;", (strNombreTabla, rut_carga)) 
    print("\n {} '{}' eliminada \n".format(strSingularMin, rut_carga))

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
            print("\n    RUT: {}\n    Nombre: {}\n    Empleado: {}\n    Relacion: {}\n    Sexo: {}\n".format(item[0], item[1], item[2], item[3], item[4]))
        print("--- Fin registros '{}' ---".format(strSingularMin))
    else:
        # Opcion 2: Buscar y mostrar
        sql_conn.miCursor.execute("SELECT * FROM ? WHERE rut_carga=?;", (strNombreTabla, PK))
        items = sql_conn.miCursor.fetchall()
        for item in items:
            print("\n    RUT: {}\n    Nombre: {}\n    Empleado: {}\n    Relacion: {}\n    Sexo: {}\n".format(item[0], item[1], item[2], item[3], item[4]))

# Controladores
#   C = Crear()
#   R = Explorar()
#   U = Actualizar()
#   D = Remover

def Crear(): # Agrega un registro. Pide los datos
    rut_carga = input("Ingrese el RUT de la Carga Familiar: ")
    NombresApellidos = input("Ingrese el nombre de la Carga Familiar: ")
    CRUD_Empleados.Obtener()
    num_Empleado = int(input("Ingrese opcion: "))
    CRUD_Relacion.Obtener()
    num_Relacion = int(input("Ingrese opcion: "))
    CRUD_Sexo.Obtener()
    num_Sexo = int(input("Ingrese opcion: "))
    Agregar(rut_carga, NombresApellidos, num_Empleado, num_Relacion, num_Sexo)

def Explorar(): # Obtener un registro. Pide PK
    print("Hay dos Opciones para esta funcion:\n    1. Listar todos\n    2. Buscar uno")
    op = int(input("Ingrese la opcion: "))
    if (op == 1):
        Obtener()
    elif (op == 2):
        Obtener(int(input("Ingrese el RUT de la Carga Familiar: ")))
    else:
        print("Opcion no valida")

def Actualizar(): # Modificar un registro. Pide PK y nuevos datos
    rut_carga = int(input("Ingrese el RUT de la Carga Familiar: "))
    # Obtener (listar y mostrar)
    Obtener(rut_carga)
    Nombre = input("Ingrese el nuevo nombre de la Carga Familiar: ")
    Modificar(rut_carga, Nombre)

def Remover(): # Eliminar un registro. Pide PK
    Eliminar(int(input("Ingrese el RUT de la Carga Familiar: ")))
