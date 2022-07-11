import sql_conn
import CRUD_Cargo
import CRUD_Sexo
import sitioEmpleado
import CRUD_ContactoEmergencia
import CRUD_CargaFamiliar
import CRUD_Credenciales
# Cambia el directorio de trabajo
#   = current file path
import os
from os.path import abspath, dirname
os.chdir(dirname(abspath(__file__)))

strPluralMin = "Empleados"
strSingularMin = "Empleado"
strNombreTabla = "EMPLEADO"

class cEmpleado:
    def __init__(self, rut, NombreApellidos, num_Sexo, direccion, telefono, num_Cargo, fechaIngreso, num_Contacto):
        self.rut = rut
        self.NombreApellidos = NombreApellidos
        self.num_Sexo = num_Sexo
        self.direccion = direccion
        self.telefono = telefono
        self.num_Cargo = num_Cargo
        self.fechaIngreso = fechaIngreso
        self.num_Contacto = num_Contacto

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
    print(CRUD_Credenciales.AgregarCredencialAuto(RUT, NombresApelidos[:20]))
    Agregar(RUT, NombresApelidos, num_Sexo, direccion, telefono, num_Cargo, fechaIngreso)
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
    Obtener(RUT)
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
    Obtener(rut)
    # obtener datos antiguos y copiarlos
    sql_conn.miCursor.execute("SELECT * FROM {};".format(strNombreTabla))
    datos = sql_conn.miCursor.fetchall()
    for item in datos:
        Nombre = input("Ingrese su nuevo Nombre: (Actual: {})".format(item[1]))
        Sexo = int(input("Ingrese su nuevo Sexo: (Actual: {})".format(item[2])))
        Direccion = input("Ingrese su nueva Direccion: (Actual: {})".format(item[3]))
        Telefono = input("Ingrese su nuevo numero de Telefono: (Actual: {})".format(item[4]))
        Modificar(rut, Nombre, Sexo, Direccion, Telefono, item[5], item[6])

def ModificarContactoDeEmergencia(rut):
    CRUD_ContactoEmergencia.Obtener(rut)
    # obtener datos antiguos y copiarlos
    sql_conn.miCursor.execute("SELECT * FROM {} WHERE num_Empleado={};".format(CRUD_ContactoEmergencia.strNombreTabla, rut))
    datos = sql_conn.miCursor.fetchall()
    for item in datos:
        Nombre = input("Ingrese su nuevo Nombre: (Actual: {})".format(item[1]))
        contacto = input("Ingrese la nueva informacion de Contacto: (Actual: {})".format(item[5]))
        CRUD_ContactoEmergencia.Modificar(rut, Nombre, contacto)

def menuCargaFamiliar():
    op = int(input("¿Que quiere hacer ahora?\n    1. Listar cargas familiares\n    2. Modificar carga existente\n    3. Crear nueva carga\n    4. Eliminar carga\n"))
    if (op == 1):
        ListarCargasFamiliares()
    elif (op == 2):
        ModificarCargaFamiliar()
    elif (op == 3):
        CrearCargaFamiliar()
    elif (op == 4):
        EliminarCargaFamiliar()

def ListarCargasFamiliares():
    sql_conn.miCursor.execute("SELECT * FROM {} WHERE num_Empleado={};".format(CRUD_CargaFamiliar.strNombreTabla, sitioEmpleado.miRUT))
    items = sql_conn.miCursor.fetchall()
    for item in items:
        print("\n    Codigo: {}\n    Nombre: {}\n    Empleado: {}\n    Relacion: {}\n    Sexo: {}\n".format(item[0], item[1], item[2], item[3], item[4]))

def ModificarCargaFamiliar():
    ListarCargasFamiliares()
    # obtener datos y mostrarlos
    codCarga = int(input("Ingrese el codigo de la carga: "))
    sql_conn.miCursor.execute("SELECT * FROM {} WHERE codCarga={};".format(CRUD_CargaFamiliar.strNombreTabla, codCarga))
    datos = sql_conn.miCursor.fetchall()
    for item in datos:
        Nombre = input("Ingrese su nuevo Nombre: (Actual: {})".format(item[1]))
        CRUD_CargaFamiliar.Modificar(codCarga, Nombre)

def CrearCargaFamiliar():
    continuar = True
    while continuar:
        print("¿Desea crear una carga familiar para ahora?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 1):
            CRUD_CargaFamiliar.Crear(sitioEmpleado.miRUT)
        else:
            continuar = False

def EliminarCargaFamiliar():
    ListarCargasFamiliares()
    codCarga = int(input("Ingrese el codigo de la carga a eliminar: "))
    CRUD_CargaFamiliar.Eliminar(codCarga)
