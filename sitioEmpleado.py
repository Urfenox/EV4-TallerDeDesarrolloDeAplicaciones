import os
import sql_conn
import Utilidades



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
        print("No disponible")
    if op == 2:
        print("No disponible")
    if op == 3:
        print("No disponible")
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
    # Buscar RUT y verificar clave con la tabla 'Credencial'
    # Recordando que al empleado se le genera un registro en la tabla 'Credencial' cuando un RRHH agrega al Empleado
    # se genera su clave en ese proceso.
    iniciarMenu()

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
