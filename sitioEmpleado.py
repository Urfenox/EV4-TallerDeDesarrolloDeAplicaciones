import os
import sql_conn

os.system("cls")

def iniciarSesion():
    rut = input("Ingrese su RUT: ")
    clave = input("Ingrese su Clave: ")
    # Buscar RUT y verificar clave con no se que tablla xd

def Empleado():
    repetir = True
    print("\n --- Bienvenido 'Empleado' ---")
    print("1. Iniciar sesion")
    print("2. Salir")
    op = int(input())
    if op == 1:
        iniciarSesion()
    if op == 2:
        repetir = False
    return False

# Ejecucion del menu
def menuEmpleado():
    while (Empleado()):
        pass