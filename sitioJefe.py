import os
import sql_conn
import Utilidades



def menuPrincipal():
    Utilidades.limpiarConsola()
    repetir = True
    print("\n --- Bienvenido 'Jefe' ---")
    print("1. No disponible")
    print("2. Salir")
    op = int(input())
    if op == 1:
        print("No disponible")
    if op == 2:
        repetir = False
    return False

# Ejecucion del menu principal (solo accesible desde inicioSesion())
def iniciarMenu():
    while (menuPrincipal()):
        pass

def inicioSesion():
    rut = input("Ingrese su RUT: ")
    clave = input("Ingrese su Clave: ")
    # Buscar RUT y verificar clave con la tabla Credenciales
    # La credencial del administrador se genera en el desarrollo. Como contraseña de fabrica
    iniciarMenu()

# Ejecucion del menu de inicio de sesion (solo accesible desde Jefe())
def menuInicioSesion():
    while (inicioSesion()):
        pass

def Jefe():
    Utilidades.limpiarConsola()
    repetir = True
    print("\n --- Bienvenido 'Jefe' ---")
    print("1. Iniciar sesion")
    print("2. Salir")
    op = int(input())
    if op == 1:
        menuInicioSesion()
    if op == 2:
        repetir = False
    return False

# Ejecucion del menu inicial (accesible solo por llamada externa)
def menuJefe():
    while (Jefe()):
        pass
