import sql_conn
import CRUD_Cargo
import CRUD_Sexo
import CRUD_Empleados
import CRUD_ContactoEmergencia
import CRUD_CargaFamiliar
import CRUD_Credenciales

strPluralMin = "Empleados"
strSingularMin = "Empleado"
strNombreTabla = "EMPLEADO"

def Agregar(RUT, NombresApelidos, num_Sexo, direccion, telefono, num_Cargo, fechaIngreso):
    sql_conn.miCursor.execute("INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?, ?);".format(strNombreTabla), (RUT, NombresApelidos, num_Sexo, direccion, telefono, num_Cargo, fechaIngreso))
    print("\n {} '{}: {}' agregado \n".format(strSingularMin, RUT, NombresApelidos))
    sql_conn.conn.commit()

def Modificar(RUT, NombresApelidos, num_Sexo, direccion, telefono, num_Cargo, fechaIngreso):
    sql_conn.miCursor.execute("UPDATE {} SET NombreApellidos=?, num_Sexo=?, direccion=?, telefono=?, num_Cargo=?, fechaIngreso=? WHERE rut=?;".format(strNombreTabla), (NombresApelidos, num_Sexo, direccion, telefono, num_Cargo, fechaIngreso, RUT))
    print("\n {} '{}: {}' modificado \n".format(strSingularMin, RUT, NombresApelidos))
    sql_conn.conn.commit()

def Eliminar(RUT):
    sql_conn.miCursor.execute("DELETE FROM {} WHERE rut={};".format(strNombreTabla, RUT)) 
    print("\n {} '{}' eliminado \n".format(strSingularMin, RUT))
    sql_conn.conn.commit()

def Obtener(PK=None):
    # Obtener lista todos los datos
    #   Opciones:
    #       Obtener(sinParametro): Lista todos los registros
    #       Obtener(Parametro=PK): Muestra el registro coincidente con la PK.
    if (PK == None):
        # Opcion 1: Buscar y mostrar todos
        sql_conn.miCursor.execute("SELECT * FROM {};".format(strNombreTabla))
        items = sql_conn.miCursor.fetchall()
        print("--- Inicio registros '{}' ---".format(strSingularMin))
        for item in items:
            print("\n    RUT: {}\n    Nombre: {}\n    Sexo: {}\n    Direccion: {}\n    Telefono: {}\n    Cargo: {}\n    Fecha Ingreso: {}\n".format(item[0], item[1], item[2], item[3], item[4], item[5], item[6]))
        print("--- Fin registros '{}' ---".format(strSingularMin))
    else:
        # Opcion 2: Buscar y mostrar
        sql_conn.miCursor.execute("SELECT * FROM {} WHERE rut={};".format(strNombreTabla, PK))
        items = sql_conn.miCursor.fetchall()
        for item in items:
            print("\n    RUT: {}\n    Nombre: {}\n    Sexo: {}\n    Direccion: {}\n    Telefono: {}\n    Cargo: {}\n    Fecha Ingreso: {}\n".format(item[0], item[1], item[2], item[3], item[4], item[5], item[6]))

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
    num_Sexo = int(input("Ingrese el Codigo del Sexo: "))
    direccion = input("Ingrese la direccion: ")
    telefono = input("Ingrese el numero telefonico: ")
    # Obtener (listar y mostrar) los cargos de la tabla 'CARGOS', luego pedir que ingrese uno.
    CRUD_Cargo.Obtener()
    num_Cargo = int(input("Ingrese el Codigo del Cargo: "))
    fechaIngreso = input("Ingrese la fecha de ingreso (dd/MM/yyyy): ")  
    # Preguntar si se desea crear un contacto de emergencia ahora.
    print("¿Desea crear un contacto de emergencia para el Empleado ahora?\n    1. Si\n    2. No")
    op = int(input("Ingrese opcion: "))
    if (op == 1):
        # crear ahora
        CRUD_ContactoEmergencia.Crear()
    continuar = True
    while continuar:
        print("¿Desea crear una carga familiar para el Empleado ahora?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 1):
            CRUD_CargaFamiliar.Crear()
        else:
            continuar = False
    # [Al finalizar] Se debera generar una contraseña para que luego el empleado pueda acceder a su 'perfil'.
    print(CRUD_Credenciales.AgregarCredencialAuto(RUT, NombresApelidos[:20]))
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

# Usos

def ModificarDatosPersonales(rut):
    CRUD_Empleados.Obtener(rut)
    # obtener datos antiguos y copiarlos
    sql_conn.miCursor.execute("SELECT * FROM {};".format(CRUD_Empleados.strNombreTabla))
    datos = sql_conn.miCursor.fetchall()
    for item in datos:
        Nombre = input("Ingrese su nuevo Nombre: (Actual: {})".format(item[1]))
        Sexo = int(input("Ingrese su nuevo Sexo: (Actual: {})".format(item[2])))
        Direccion = input("Ingrese su nueva Direccion: (Actual: {})".format(item[3]))
        Telefono = input("Ingrese su nuevo numero de Telefono: (Actual: {})".format(item[4]))
        CRUD_Empleados.Modificar(rut, Nombre, Sexo, Direccion, Telefono, item[5], item[6])
def ModificarContactoDeEmergencia(rut):
    CRUD_ContactoEmergencia.Obtener(rut)
    # obtener datos antiguos y copiarlos
    sql_conn.miCursor.execute("SELECT * FROM {} WHERE num_Empleado=?;".format(CRUD_ContactoEmergencia.strNombreTabla), (rut))
    datos = sql_conn.miCursor.fetchall()
    for item in datos:
        Nombre = input("Ingrese su nuevo Nombre: (Actual: {})".format(item[1]))
        Sexo = int(input("Ingrese el nuevo Sexo: (Actual: {})".format(item[3])))
        contacto = input("Ingrese la nueva informacion de Contacto: (Actual: {})".format(item[5]))
        CRUD_ContactoEmergencia.Modificar(Nombre, item[2], Sexo, rut, contacto)
def ModificarCargaFamiliar():
    rut_carga = int(input("Ingrese el RUT de la Carga Familiar: "))
    # obtener datos antiguos y copiarlos
    sql_conn.miCursor.execute("SELECT * FROM {} WHERE num_Empleado=?;".format(CRUD_CargaFamiliar.strNombreTabla), (rut_carga))
    datos = sql_conn.miCursor.fetchall()
    for item in datos:
        Nombre = input("Ingrese su nuevo Nombre: (Actual: {})".format(item[1]))
        CRUD_CargaFamiliar.Modificar(rut_carga, Nombre)
