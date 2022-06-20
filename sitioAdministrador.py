import os
import sql_conn

os.system("cls")

def iniciarSesion():
    clave = input("Ingrese Clave: ")
    # Buscar y verificar. bla bla

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

# Ejecucion del menu
def menuAdministrador():
    while (Administrador()):
        pass