from asyncio.windows_events import NULL
import sql_conn
import CRUD_Cargo
import CRUD_Sexo
import CRUD_ContactoEmergencia
import CRUD_CargaFamiliar

strPluralMin = "Empleados"
strSingularMin = "Empleado"
strNombreTabla = "EMPLEADO"

def Agregar(RUT, NombresApelidos, num_Sexo, direccion, telefono, num_Cargo, fechaIngreso):
    sql_conn.miCursor.execute("INSERT INTO ? VALUES (?, ?, ?, ?, ?, ?, ?);", (strNombreTabla, RUT, NombresApelidos, num_Sexo, direccion, telefono, num_Cargo, fechaIngreso))
    print("\n {} '{}: {}' agregado \n".format(strSingularMin, RUT, NombresApelidos))

def Modificar(RUT, NombresApelidos, num_Sexo, direccion, telefono, num_Cargo, fechaIngreso):
    sql_conn.miCursor.execute("UPDATE ? SET NombreApellidos=?, num_Sexo=?, direccion=?, telefono=?, num_Cargo=?, fechaIngreso=? WHERE rut=?;", (strNombreTabla, NombresApelidos, num_Sexo, direccion, telefono, num_Cargo, fechaIngreso, RUT))
    print("\n {} '{}: {}' modificado \n".format(strSingularMin, RUT, NombresApelidos))

def Eliminar(RUT):
    sql_conn.miCursor.execute("DELETE FROM ? WHERE rut=?;", (strNombreTabla, RUT)) 
    print("\n {} '{}' eliminado \n".format(strSingularMin, RUT))

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
            print("\n    RUT: {}\n    NombreApellidos: {}\n    Sexo: {}\n    Direccion: {}\n    Telefono: {}\n    Cargo: {}\n    Fecha Ingreso: {}\n".format(item[0], item[1], item[2], item[3], item[4], item[5], item[6]))
        print("--- Fin registros '{}' ---".format(strSingularMin))
    else:
        # Opcion 2: Buscar y mostrar
        sql_conn.miCursor.execute("SELECT * FROM ? WHERE rut=?;", (strNombreTabla, PK))
        items = sql_conn.miCursor.fetchall()
        for item in items:
            print("\n    RUT: {}\n    NombreApellidos: {}\n    Sexo: {}\n    Direccion: {}\n    Telefono: {}\n    Cargo: {}\n    Fecha Ingreso: {}\n".format(item[0], item[1], item[2], item[3], item[4], item[5], item[6]))

# Controladores
#   C = Crear()
#   R = Explorar()
#   U = Actualizar()
#   D = Remover()

def Crear(): # Agrega un registro. Pide los datos
    RUT = int(input("Ingrese el RUT (solo numeros): "))
    NombresApelidos = input("Ingrese los Nombres y Apellidos: ")
    # Obtener (listar y mostrar) los sexos de la tabla 'SEXO', luego pedir que ingrese uno.
    CRUD_Sexo.Obtener()
    num_Sexo = int(input("Ingrese opcion: "))
    direccion = input("Ingrese la direccion: ")
    telefono = input("Ingrese el numero telefonico: ")
    # Obtener (listar y mostrar) los cargos de la tabla 'CARGOS', luego pedir que ingrese uno.
    CRUD_Cargo.Obtener()
    num_Cargo = int(input("Ingrese el numero del cargo: "))
    fechaIngreso = input("Ingrese la fecha de ingreso (dd/MM/yyyy): ")
    
    # Preguntar si se desea crear un contacto de emergencia ahora.
    print("¿Desea crear un contacto de emergencia para el Empleado ahora?\n    1. Si\n    2. No")
    op = int(input("Ingrese opcion: "))
    if (op == 1):
        # crear ahora
        CRUD_ContactoEmergencia.Crear()

    print("¿Desea crear una carga familiar para el Empleado ahora?\n    1. Si\n    2. No")
    op = int(input("Ingrese opcion: "))
    if (op == 1):
        # crear ahora
        CRUD_CargaFamiliar.Crear()

    # Obtener (listar y mostrar) los contactos de la tabla 'CONTACTO_EMERGENCIA', luego pedir que ingrese uno.
    CRUD_ContactoEmergencia.Obtener()
    num_Contacto = int(input("Ingrese opcion: "))
    # [Al finalizar] Se debera generar una contraseña para que luego el empleado pueda acceder a su 'perfil'.
    #   Esta clave debe guardarse en md5 en la tabla 'Credenciales'
    Agregar(RUT, NombresApelidos, num_Sexo, direccion, telefono, num_Cargo, fechaIngreso)

def Explorar(): # Obtener un registro. Pide PK
    print("Hay dos Opciones para esta funcion:\n    1. Listar todos\n    2. Buscar uno")
    op = int(input("Ingrese la opcion: "))
    if (op == 1):
        Obtener()
    elif (op == 2):
        Obtener(int(input("Ingrese el RUT del Empleado: ")))
    else:
        print("Opcion no valida")

def Actualizar(): # Modificar un registro. Pide PK y nuevos datos
    RUT = int(input("Ingrese el RUT del Empleado: "))
    # Obtener (listar y mostrar)
    CRUD_Sexo.Obtener(RUT)
    NombresApelidos = input("Ingrese los nuevos Nombres y Apellidos: ")
    # Obtener (listar y mostrar)
    CRUD_Sexo.Obtener()
    num_Sexo = int(input("Ingrese opcion: "))
    direccion = input("Ingrese la nueva direccion: ")
    telefono = input("Ingrese el nuevo numero telefonico: ")
    # Obtener (listar y mostrar)
    CRUD_Cargo.Obtener()
    num_Cargo = int(input("Ingrese el numero del nuevo cargo: "))
    fechaIngreso = input("Ingrese la nueva fecha de ingreso (dd/MM/yyyy): ")
    Modificar(RUT, NombresApelidos, num_Sexo, direccion, telefono, num_Cargo, fechaIngreso)

def Remover(): # Eliminar un registro. Pide PK
    Eliminar(int(input("Ingrese el RUT del Empleado: ")))
