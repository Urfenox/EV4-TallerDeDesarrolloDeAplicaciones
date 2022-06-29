from asyncio.windows_events import NULL
import sql_conn
import CRUD_Departamento

strPluralMin = "Cargos"
strSingularMin = "Cargo"
strNombreTabla = "CARGO"

def Agregar(Nombre, num_Departamento):
    # verificar en que codigo van
    sql_conn.miCursor.execute("SELECT * FROM {};".format(strNombreTabla))
    contenido = sql_conn.miCursor.fetchall()
    contadorActual = len(contenido)
    sql_conn.miCursor.execute("INSERT INTO {} VALUES (?, ?, ?);".format(strNombreTabla), (contadorActual, Nombre, num_Departamento))
    print("\n {} '{}: {}: {}' agregado \n".format(strSingularMin, Nombre, contadorActual, num_Departamento))
    sql_conn.conn.commit()

def Modificar(codCargo, Nombre):
    sql_conn.miCursor.execute("UPDATE {} SET nombreCargo=? WHERE codCargo=?;".format(strNombreTabla), (Nombre, codCargo))
    print("\n {} '{}: {}' modificado \n".format(strSingularMin, codCargo, Nombre))
    sql_conn.conn.commit()

def Eliminar(codCargo):
    sql_conn.miCursor.execute("DELETE FROM {} WHERE codCargo=?;".format(strNombreTabla), (codCargo)) 
    print("\n {} '{}' eliminado \n".format(strSingularMin, codCargo))
    sql_conn.conn.commit()

def Obtener(PK=NULL):
    # Obtener lista todos los datos
    #   Opciones:
    #       Obtener(sinParametro): Lista todos los registros
    #       Obtener(Parametro=PK): Muestra el registro coincidente con la PK.
    if (PK == NULL):
        # Opcion 1: Buscar y mostrar todos
        sql_conn.miCursor.execute("SELECT * FROM {};".format(strNombreTabla))
        items = sql_conn.miCursor.fetchall()
        print("--- Inicio registros '{}' ---".format(strSingularMin))
        for item in items:
            print("\n    Codigo: {}\n    Nombre: {}\n    Departamento: {}\n".format(item[0], item[1], item[2]))
        print("--- Fin registros '{}' ---".format(strSingularMin))
    else:
        # Opcion 2: Buscar y mostrar
        sql_conn.miCursor.execute("SELECT * FROM {} WHERE codCargo=?;".format(strNombreTabla), (PK))
        items = sql_conn.miCursor.fetchall()
        for item in items:
            print("\n    Codigo: {}\n    Nombre: {}\n    Departamento: {}\n".format(item[0], item[1], item[2]))

# Controladores
#   C = Crear()
#   R = Explorar()
#   U = Actualizar()
#   D = Remover()

def Crear(): # Agrega un registro. Pide los datos
    Nombre = input("Ingrese el nombre del Cargo: ")
    CRUD_Departamento.Obtener()
    codDepartamento = int(input("Ingrese el Codigo del Departamento: "))
    Agregar(Nombre, codDepartamento)

def Explorar(): # Obtener un registro. Pide PK
    print("Hay dos Opciones para esta funcion:\n    1. Listar todos\n    2. Buscar uno")
    op = int(input("Ingrese la opcion: "))
    if (op == 1):
        Obtener()
    elif (op == 2):
        Obtener(int(input("Ingrese el Codigo del Cargo: ")))
    else:
        print("Opcion no valida")

def Actualizar(): # Modificar un registro. Pide PK y nuevos datos
    codCargo = int(input("Ingrese el Codigo del Cargo: "))
    # Obtener (listar y mostrar)
    Obtener(codCargo)
    Nombre = input("Ingrese el nuevo nombre del Cargo: ")
    Modificar(codCargo, Nombre)

def Remover(): # Eliminar un registro. Pide PK
    Eliminar(int(input("Ingrese el Codigo del Cargo: ")))
