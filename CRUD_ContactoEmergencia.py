from asyncio.windows_events import NULL
import sql_conn
import CRUD_Relacion
import CRUD_Cargo
import CRUD_Empleados

strPluralMin = "Contactos de Emergencias"
strSingularMin = "Contacto de Emergencia"
strNombreTabla = "CONTACTO_EMERGENCIA"

def Agregar(NombreApellido, num_Relacion, num_Sexo, num_Empleado, contacto):
    # verificar en que codigo van
    sql_conn.miCursor.execute("SELECT * FROM {};".format(strNombreTabla))
    contenido = sql_conn.miCursor.fetchall()
    contadorActual = len(contenido)
    sql_conn.miCursor.execute("INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?);".format(strNombreTabla), (contadorActual, NombreApellido, num_Relacion, num_Sexo, num_Empleado, contacto))
    print("\n {} '{}: {}: {}' agregado \n".format(strSingularMin, contadorActual, NombreApellido, num_Empleado))
    sql_conn.conn.commit()

def Modificar(codContacto, Nombre, Contacto):
    sql_conn.miCursor.execute("UPDATE {} SET NombreApellido=?, contacto=? WHERE codContacto=?;".format(strNombreTabla), (Nombre, Contacto, codContacto))
    print("\n {} '{}: {}' modificado \n".format(strSingularMin, codContacto, Nombre))

def Eliminar(codContacto):
    sql_conn.miCursor.execute("DELETE FROM {} WHERE codContacto=?;".format(strNombreTabla), (codContacto)) 
    print("\n {} '{}' eliminado \n".format(strSingularMin, codContacto))

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
            print("\n    Codigo: {}\n    Nombre: {}\n    Relacion: {}\n    Sexo: {}\n    Empleado: {}\n    Contacto: {}\n".format(item[0], item[1], item[2], item[3], item[4], item[5]))
        print("--- Fin registros '{}' ---".format(strSingularMin))
    else:
        # Opcion 2: Buscar y mostrar
        sql_conn.miCursor.execute("SELECT * FROM {} WHERE codContacto=?;".format(strNombreTabla), (PK))
        items = sql_conn.miCursor.fetchall()
        for item in items:
            print("\n    Codigo: {}\n    Nombre: {}\n    Relacion: {}\n    Sexo: {}\n    Empleado: {}\n    Contacto: {}\n".format(item[0], item[1], item[2], item[3], item[4], item[5]))

# Controladores
#   C = Crear()
#   R = Explorar()
#   U = Actualizar()
#   D = Remover

def Crear(): # Agrega un registro. Pide los datos
    NombreApellido = input("Ingrese los Nombres y Apellidos: ")
    CRUD_Relacion.Obtener()
    num_Relacion = int(input("Ingrese el Codigo de la Relacion: "))
    CRUD_Cargo.Obtener()
    num_Sexo = int(input("Ingrese opcion: "))
    CRUD_Empleados.Obtener()
    num_Empleado = int(input("Ingrese el Codigo del Empleado: "))
    contacto = input("Ingrese informacion de contacto: ")
    Agregar(NombreApellido, num_Relacion, num_Sexo, num_Empleado, contacto)

def Explorar(): # Obtener un registro. Pide PK
    print("Hay dos Opciones para esta funcion:\n    1. Listar todos\n    2. Buscar uno")
    op = int(input("Ingrese la opcion: "))
    if (op == 1):
        Obtener()
    elif (op == 2):
        Obtener(int(input("Ingrese el Codigo del Contacto: ")))
    else:
        print("Opcion no valida")

def Actualizar(): # Modificar un registro. Pide PK y nuevos datos
    codContacto = int(input("Ingrese el Codigo del Contacto: "))
    # Obtener (listar y mostrar)
    Obtener(codContacto)
    Nombre = input("Ingrese el nuevo nombre del Contacto: ")
    Contacto = input("Ingrese el nuevo Contacto: ")
    Modificar(codContacto, Nombre, Contacto)

def Remover(): # Eliminar un registro. Pide PK
    Eliminar(int(input("Ingrese el Codigo del Contacto: ")))
