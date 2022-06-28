import os
import sql_conn
import CRUD_Administrador
import Utilidades



def iniciarSesion():
    clave = input("Ingrese Clave de Administrador: ")
    if (clave == Utilidades.claveAdmin):
        CRUD_Administrador.iniciarMenu()

def Administrador():
    Utilidades.limpiarConsola()
    repetir = True
    print("\n --- Bienvenido 'Administrador' ---")
    print("1. Iniciar sesion")
    print("2. Salir")
    op = int(input())
    if op == 1:
        iniciarSesion()
    if op == 2:
        repetir = False
    return False

# Ejecucion del menu inicial (accesible solo por llamada externa)
def menuAdministrador():
    while (Administrador()):
        pass
