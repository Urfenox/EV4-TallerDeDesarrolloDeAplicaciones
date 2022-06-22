import os
import sql_conn
import CRUD_Administrador

os.system("cls")

def iniciarSesion():
    clave = input("Ingrese Clave: ")
    # Buscar y verificar. bla bla
    # La credencial del administrador se genera en el desarrollo. Como contraseña de fabrica
    CRUD_Administrador.iniciarMenu()

def Administrador():
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