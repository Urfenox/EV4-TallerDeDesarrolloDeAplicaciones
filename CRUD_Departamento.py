from asyncio.windows_events import NULL
import sql_conn

strPluralMin = "Departamentos"
strSingularMin = "Departamento"
strNombreTabla = "DEPARTAMENTO"

def Agregar(Nombre, num_Area):
    # verificar en que codigo van
    sql_conn.miCursor.execute("SELECT * FROM ?;", (strNombreTabla))
    contenido = sql_conn.miCursor.fetchall()
    contadorActual = len(contenido)
    sql_conn.miCursor.execute("INSERT INTO ? VALUES (?, ?, ?);", (strNombreTabla, contadorActual, Nombre, num_Area))
    print("\n {} '{}: {}: {}' agregado \n".format(strSingularMin, contadorActual, Nombre, num_Area))
    sql_conn.conn.commit()

def Modificar(codDepartamento, Nombre):
    sql_conn.miCursor.execute("UPDATE ? SET Nombre=? WHERE codDepartamento=?;", (strNombreTabla, Nombre, codDepartamento))
    print("\n {} '{}: {}' modificado \n".format(strSingularMin, codDepartamento, Nombre))

def Eliminar(codDepartamento):
    sql_conn.miCursor.execute("DELETE FROM ? WHERE codDepartamento=?;", (strNombreTabla, codDepartamento)) 
    print("\n {} '{}' eliminado \n".format(strSingularMin, codDepartamento))

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
            print("\n    Codigo: {}\n    Nombre: {}\n    Area: {}\n".format(item[0], item[1], item[2]))
        print("--- Fin registros '{}' ---".format(strSingularMin))
    else:
        # Opcion 2: Buscar y mostrar
        sql_conn.miCursor.execute("SELECT * FROM ? WHERE codDepartamento=?;", (strNombreTabla, PK))
        items = sql_conn.miCursor.fetchall()
        for item in items:
            print("\n    Codigo: {}\n    Nombre: {}\n    Area: {}\n".format(item[0], item[1], item[2]))

# Controladores
#   C = Crear()
#   R = Explorar()
#   U = Actualizar()
#   D = Remover()

def Crear(): # Agrega un registro. Pide los datos
    Agregar(input("Ingrese el nombre del Departamento: "), int(input("Ingrese el Codigo del Area: ")))

def Explorar(): # Obtener un registro. Pide PK
    print("Hay dos Opciones para esta funcion:\n    1. Listar todos\n    2. Buscar uno")
    op = int(input("Ingrese la opcion: "))
    if (op == 1):
        Obtener()
    elif (op == 2):
        Obtener(int(input("Ingrese el Codigo del Departamento: ")))
    else:
        print("Opcion no valida")

def Actualizar(): # Modificar un registro. Pide PK y nuevos datos
    codDepartamento = int(input("Ingrese el Codigo del Departamento: "))
    # Obtener (listar y mostrar)
    Obtener(codDepartamento)
    Nombre = input("Ingrese el nuevo nombre del Departamento: ")
    Modificar(codDepartamento, Nombre)

def Remover(): # Eliminar un registro. Pide PK
    Eliminar(int(input("Ingrese el Codigo del Departamento: ")))
