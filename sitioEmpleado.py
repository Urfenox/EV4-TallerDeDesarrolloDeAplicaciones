import Utilidades
import CRUD_Empleados
import CRUD_Credenciales

miRUT = None

def menuPrincipal():
    Utilidades.limpiarConsola()
    repetir = True
    print("\n --- Bienvenido 'Empleado' ---")
    print("1. Modificar Datos Personales")
    print("2. Modificar Contacto de Emergencia")
    print("3. Modificar Cargas Familiares")
    print("4. Salir")
    op = int(input())
    if op == 1:
        CRUD_Empleados.ModificarDatosPersonales(miRUT)
    if op == 2:
        CRUD_Empleados.ModificarContactoDeEmergencia(miRUT)
    if op == 3:
        CRUD_Empleados.ModificarCargaFamiliar()
    if op == 4:
        repetir = False
    return False

# Ejecucion del menu principal (solo accesible desde inicioSesion())
def iniciarMenu():
    while (menuPrincipal()):
        pass

def inicioSesion():
    rut = input("Ingrese su RUT: ")
    clave = input("Ingrese su Clave: ")
    miRUT = rut
    if (CRUD_Credenciales.VerificarCredencial(rut, clave) == True):
        iniciarMenu()
    else:
        print("Credenciales incorrectas.")

# Ejecucion del menu de inicio de sesion (solo accesible desde Empleado())
def menuInicioSesion():
    while (inicioSesion()):
        pass

def Empleado():
    Utilidades.limpiarConsola()
    repetir = True
    print("\n --- Bienvenido 'Empleado' ---")
    print("1. Iniciar sesion")
    print("2. Salir")
    op = int(input())
    if op == 1:
        menuInicioSesion()
    if op == 2:
        repetir = False
    return False

# Ejecucion del menu inicial (accesible solo por llamada externa)
def menuEmpleado():
    while (Empleado()):
        pass
