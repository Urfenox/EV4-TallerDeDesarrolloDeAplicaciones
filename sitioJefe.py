import os
import sql_conn

os.system("cls")

def iniciarSesion():
    rut = input("Ingrese su RUT: ")
    clave = input("Ingrese su Clave: ")
    # Buscar RUT y verificar. bla bla

def Jefe():
    repetir = True
    print("\n --- Bienvenido 'Jefe' ---")
    print("1. Iniciar sesion")
    print("2. Salir")
    op = int(input())
    if op == 1:
        iniciarSesion()
    if op == 2:
        repetir = False
    return False

# Ejecucion del menu
def menuJefe():
    while (Jefe()):
        pass