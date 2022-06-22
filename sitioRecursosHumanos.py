import os
import sql_conn
import CRUD_Empleados

os.system("cls")

def listarEmpleados():
    print("No disponible")

def agregarEmpleados():
    print("Parcialmente disponible")
    RUT = int(input("Ingrese el RUT (solo numeros): "))
    Nombre = input("Ingrese los Nombres y Apellidos: ")
    Sexo = int(input("Ingrese 1 para Hombre o 2 para Mujer: "))
    Direccion = input("Ingrese la direccion: ")
    Telefono = input("Ingrese el numero telefonico: ")
    # Obtener (listar y mostrar) los cargos de la tabla 'CARGOS', luego pedir que ingrese uno.
    Cargo = int(input("Ingrese el numero del cargo: "))
    FechaIngreso = input("Ingrese la fecha de ingreso: ")
    # Para seleccionar un contacto, este debera estar creado.
    #   Se debe crear un contacto. Aqui mismo.
    #   Tambien se deberan agregar las cargas familiares. Aqui mismo.
    Contacto = ""
    # OJO: Si algun dato se ingresa mal y el programa se muere, los datos deberan ser ingresados otra vez.
    #   Esto resultara en algo terriblemente horrible para el usuario, quiza crear un .txt con los datos temporalmente, luego revisar si hay algun Empleado que haya quedado guardado.
    #   Si es asi, entonces se cargan los datos y se continua desde donde lo dejo. (Opcional)
    #   Opcional obligatorio, para las 'copias de seguridad' se tendra que hacer.
    # ...
    # [Al finalizar] Se debera generar una contraseña para que luego el empleado pueda acceder a su 'perfil'.
    #   Esta clave debe guardarse en md5 en la tabla 'Credenciales'
    # CRUD_Empleados.Agregar(RUT, Nombre, Sexo, Direccion, Telefono, Cargo, FechaIngreso, Contacto)

def buscarEmpleados():
    print("No disponible")

def eliminarEmpleados():
    print("No disponible")

def modificarEmpleados():
    print("No disponible")

def menuPrincipal():
    repetir = True
    print("\n --- Bienvenido a 'Recursos Humanos' ---")
    print("1. Listar Empleados")
    print("2. Agregar Empleado")
    print("3. Buscar Empleado")
    print("4. Eliminar Empleado")
    print("5. Modificar Empleado")
    print("6. Salir")
    op = int(input())
    if op == 1:
        listarEmpleados()
    if op == 2:
        agregarEmpleados()
    if op == 3:
        buscarEmpleados()
    if op == 4:
        eliminarEmpleados()
    if op == 5:
        modificarEmpleados()
    if op == 6:
        repetir = False
    return False

# Ejecucion del menu principal (solo accesible desde inicioSesion())
def iniciarMenu():
    while (menuPrincipal()):
        pass

def inicioSesion():
    clave = input("Ingrese Clave: ")
    # Buscar y verificar. bla bla
    # La credencial de RecursosHumanos se genera en el desarrollo. Como contraseña de fabrica
    iniciarMenu()
    
# Ejecucion del menu de inicio de sesion (solo accesible desde RecursosHumanos())
def menuInicioSesion():
    while (inicioSesion()):
        pass

def RecursosHumanos():
    repetir = True
    print("\n --- Bienvenido a 'Recursos Humanos' ---")
    print("1. Iniciar Sesion")
    print("2. Salir")
    op = int(input())
    if op == 1:
        menuInicioSesion()
    if op == 2:
        repetir = False
    return False

# Ejecucion del menu inicial (accesible solo por llamada externa)
def menuRecursosHumanos():
    while (RecursosHumanos()):
        pass