import sql_conn
import CRUD_Empleados
import CRUD_Relacion
import CRUD_Sexo

strPluralMin = "Cargas Camiliares"
strSingularMin = "Carga Familiar"
strNombreTabla = "CARGA_FAMILIAR"

class cCargaFamiliar:
    def __init__(self, codDepartamento, Nombre, num_Area):
        self.codArea = codDepartamento
        self.Nombre = Nombre
        self.num_Area = num_Area

def Agregar(NombresApellidos, num_Empleado, num_Relacion, num_Sexo):
    # verificar en que codigo van
    sql_conn.miCursor.execute("SELECT * FROM {};".format(strNombreTabla))
    contenido = sql_conn.miCursor.fetchall()
    contadorActual = len(contenido)
    sql_conn.miCursor.execute("INSERT INTO {} VALUES (?, ?, ?, ?, ?);".format(strNombreTabla), (contadorActual, NombresApellidos, num_Empleado, num_Relacion, num_Sexo))
    print("\n {} '{}: {}: {}' agregada \n".format(strSingularMin, contadorActual, NombresApellidos, num_Empleado))
    sql_conn.conn.commit()

def Modificar(codCarga, Nombre):
    sql_conn.miCursor.execute("UPDATE {} SET NombresApellidos=? WHERE codCarga=?;".format(strNombreTabla), (Nombre, codCarga))
    print("\n {} '{}: {}' modificado \n".format(strSingularMin, codCarga, Nombre))
    sql_conn.conn.commit()

def Eliminar(codCarga):
    sql_conn.miCursor.execute("DELETE FROM {} WHERE codCarga={};".format(strNombreTabla, codCarga)) 
    print("\n {} '{}' eliminada \n".format(strSingularMin, codCarga))
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
            print("\n    Codigo: {}\n    Nombre: {}\n    Empleado: {}\n    Relacion: {}\n    Sexo: {}\n".format(item[0], item[1], item[2], item[3], item[4]))
        print("--- Fin registros '{}' ---".format(strSingularMin))
    else:
        # Opcion 2: Buscar y mostrar
        sql_conn.miCursor.execute("SELECT * FROM {} WHERE codCarga={};".format(strNombreTabla, PK))
        items = sql_conn.miCursor.fetchall()
        for item in items:
            print("\n    Codigo: {}\n    Nombre: {}\n    Empleado: {}\n    Relacion: {}\n    Sexo: {}\n".format(item[0], item[1], item[2], item[3], item[4]))

# Controladores
#   C = Crear()
#   R = Explorar()
#   U = Actualizar()
#   D = Remover

def Crear(num_Empleado): # Agrega un registro. Pide los datos
    NombresApellidos = input("Ingrese el nombre de la Carga Familiar: ")
    CRUD_Empleados.Obtener()
    if (num_Empleado == None):
        num_Empleado = int(input("Ingrese el Codigo del Empleado: "))
    CRUD_Relacion.Obtener()
    num_Relacion = int(input("Ingrese el Codigo de la Relacion: "))
    CRUD_Sexo.Obtener()
    num_Sexo = int(input("Ingrese el Codigo del Sexo: "))
    Agregar(NombresApellidos, num_Empleado, num_Relacion, num_Sexo)

def Explorar(): # Obtener un registro. Pide PK
    print("Hay dos Opciones para esta funcion:\n    1. Listar todos\n    2. Buscar uno")
    op = int(input("Ingrese la opcion: "))
    if (op == 1):
        Obtener()
    elif (op == 2):
        Obtener(int(input("Ingrese el Codigo de la Carga Familiar: ")))
    else:
        print("Opcion no valida")

def Actualizar(): # Modificar un registro. Pide PK y nuevos datos
    codCarga = int(input("Ingrese el Codigo de la Carga Familiar: "))
    # Obtener (listar y mostrar)
    Obtener(codCarga)
    Nombre = input("Ingrese el nuevo nombre de la Carga Familiar: ")
    Modificar(codCarga, Nombre)

def Remover(): # Eliminar un registro. Pide PK
    Eliminar(int(input("Ingrese el Codigo de la Carga Familiar: ")))
