import configurador
import Utilidades
import sitioRecursosHumanos
import sitioEmpleado
import sitioJefe
import sitioAdministrador
# Cambia el directorio de trabajo
#   = current file path
import os
from os.path import abspath, dirname
os.chdir(dirname(abspath(__file__)))



Utilidades.limpiarConsola()

# Menu principal
def menuPrincipal():
    Utilidades.limpiarConsola()
    repetir = True
    print("\n --- Bienvenido al 'Listado de Usuarios' ---")
    print("1. Soy Recursos Humanos")
    print("2. Soy Empleado")
    print("3. Soy Jefe")
    print("4. Soy Administrador")
    print("5. Salir")
    op = int(input("Ingrese una opcion: "))
    if op == 1:
        sitioRecursosHumanos.menuRecursosHumanos()
    if op == 2:
        sitioEmpleado.menuEmpleado()
    if op == 3:
        sitioJefe.menuJefe()
    if op == 4:
        sitioAdministrador.menuAdministrador()
    if op == 5:
        repetir = False
    return repetir

# Ejecucion del menu
def iniciarMenu():
    while (menuPrincipal()):
        pass
    Utilidades.salirPrograma()

def Principal():
    configurador.verificarIntegridad()
    iniciarMenu()

Principal()
