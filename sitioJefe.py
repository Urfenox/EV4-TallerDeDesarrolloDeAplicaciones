import Utilidades
import CRUD_Credenciales
# Cambia el directorio de trabajo
#   = current file path
import os
from os.path import abspath, dirname
os.chdir(dirname(abspath(__file__)))



def menuPrincipal():
    Utilidades.limpiarConsola()
    repetir = True
    print("\n --- Bienvenido 'Jefe' ---")
    print("1. No disponible")
    print("2. Salir")
    op = int(input())
    if op == 1:
        print("No disponible")
        Utilidades.pausarContinuar()
    if op == 2:
        repetir = False
    return repetir

# Ejecucion del menu principal (solo accesible desde inicioSesion())
def iniciarMenu():
    while (menuPrincipal()):
        pass

def inicioSesion():
    rut = input("Ingrese su RUT: ")
    clave = input("Ingrese su Clave: ")
    if (CRUD_Credenciales.VerificarCredencial(rut, clave) == True):
        iniciarMenu()
    else:
        print("Credenciales incorrectas.")

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
    return repetir

# Ejecucion del menu inicial (accesible solo por llamada externa)
def menuJefe():
    while (Jefe()):
        pass
