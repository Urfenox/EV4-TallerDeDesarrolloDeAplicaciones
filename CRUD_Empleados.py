from asyncio.windows_events import NULL
import sql_conn

strPluralMin = "Empleados"
strSingularMin = "Empleado"
strNombreTabla = "EMPLEADO"

def Agregar(RUT, NombresApelidos, num_Sexo, direccion, telefono, num_Cargo, fechaIngreso, num_Contacto):
    sql_conn.miCursor.execute("INSERT INTO ? VALUES (?, ?, ?, ?, ?, ?, ?, ?);", (strNombreTabla, RUT, NombresApelidos, num_Sexo, direccion, telefono, num_Cargo, fechaIngreso, num_Contacto))
    print("\n {} '{}: {}' agregado \n".format(strSingularMin, RUT, NombresApelidos))

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
            print("\n    RUT: {}\n    NombreApellidos: {}\n    Sexo: {}\n    Direccion: {}\n    Telefono: {}\n    Cargo: {}\n    Fecha Ingreso: {}\n    Contacto Emergencia: {}\n".format(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]))
        print("--- Fin registros '{}' ---".format(strSingularMin))
    else:
        # Opcion 2: Buscar y mostrar
        sql_conn.miCursor.execute("SELECT * FROM ? WHERE rut=?;", (strNombreTabla, PK))
        items = sql_conn.miCursor.fetchall()
        for item in items:
            print("\n    RUT: {}\n    NombreApellidos: {}\n    Sexo: {}\n    Direccion: {}\n    Telefono: {}\n    Cargo: {}\n    Fecha Ingreso: {}\n    Contacto Emergencia: {}\n".format(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]))
