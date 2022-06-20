import os
import sql_conn

os.system("cls")

def listarEmpleados():
    print("No disponible")

def agregarEmpleados():
    print("No disponible")

def buscarEmpleados():
    print("No disponible")

def eliminarEmpleados():
    print("No disponible")

def modificarEmpleados():
    print("No disponible")

def RecursosHumanos():
    repetir = True
    print("\n --- Bienvenido a 'Recursos Humanos' ---")
    print("1. Listar Empleados")
    print("2. Agregar Empleado")
    print("3. Buscar Empleado")
    print("4. Eliminar Empleado")
    print("5. Modificar Empleado")
    print("6. Salir")
    op = int(input())
    if op == 1:
        listarEmpleados()
    if op == 2:
        agregarEmpleados()
    if op == 3:
        buscarEmpleados()
    if op == 4:
        eliminarEmpleados()
    if op == 5:
        modificarEmpleados()
    if op == 6:
        repetir = False
    return False

# Ejecucion del menu
def menuRecursosHumanos():
    while (RecursosHumanos()):
        pass