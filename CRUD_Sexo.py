import sql_conn

strPluralMin = "Sexos"
strSingularMin = "Sexo"
strNombreTabla = "SEXO"

def Agregar(Nombre):
    # verificar en que codigo van
    sql_conn.miCursor.execute("SELECT * FROM {};".format(strNombreTabla))
    contenido = sql_conn.miCursor.fetchall()
    contadorActual = len(contenido)
    sql_conn.miCursor.execute("INSERT INTO {} VALUES (?, ?);".format(strNombreTabla), (contadorActual, Nombre))
    print("\n {} '{}: {}' agregado \n".format(strSingularMin, Nombre, contadorActual))
    sql_conn.conn.commit()

def Modificar(codSexo, Nombre):
    sql_conn.miCursor.execute("UPDATE {} SET Nombre=? WHERE codSexo=?;".format(strNombreTabla), (Nombre, codSexo))
    print("\n {} '{}: {}' modificado \n".format(strSingularMin, codSexo, Nombre))
    sql_conn.conn.commit()

def Eliminar(codSexo):
    sql_conn.miCursor.execute("DELETE FROM {} WHERE codSexo={};".format(strNombreTabla, codSexo)) 
    print("\n {} '{}' eliminado \n".format(strSingularMin, codSexo))
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
            print("\n    Codigo: {}\n    Nombre: {}\n".format(item[0], item[1]))
        print("--- Fin registros '{}' ---".format(strSingularMin))
    else:
        # Opcion 2: Buscar y mostrar
        sql_conn.miCursor.execute("SELECT * FROM {} WHERE codSexo={};".format(strNombreTabla, PK))
        items = sql_conn.miCursor.fetchall()
        for item in items:
            print("\n    Codigo: {}\n    Nombre: {}\n".format(item[0], item[1]))

# Controladores
#   C = Crear()
#   R = Explorar()
#   U = Actualizar()
#   D = Remover()

def Crear(): # Agrega un registro. Pide los datos
    Nombre = input("Ingrese el nombre del Sexo: ")
    Agregar(Nombre)

def Explorar(): # Obtener un registro. Pide PK
    print("Hay dos Opciones para esta funcion:\n    1. Listar todos\n    2. Buscar uno")
    op = int(input("Ingrese la opcion: "))
    if (op == 1):
        Obtener()
    elif (op == 2):
        Obtener(int(input("Ingrese el Codigo del Sexo: ")))
    else:
        print("Opcion no valida")

def Actualizar(): # Modificar un registro. Pide PK y nuevos datos
    codSexo = int(input("Ingrese el Codigo del Sexo: "))
    # Obtener (listar y mostrar)
    Obtener(codSexo)
    Nombre = input("Ingrese el nuevo nombre del Sexo: ")
    Modificar(codSexo, Nombre)

def Remover(): # Eliminar un registro. Pide PK
    Eliminar(int(input("Ingrese el Codigo del Sexo: ")))
