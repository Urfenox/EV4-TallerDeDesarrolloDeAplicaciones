import os
import sql_conn
import CRUD_Empleados

strAdministracion = "Administracion"
strAdministrador = "Administrador"

def menuPrincipal():
    repetir = True
    print("\n --- Bienvenido al 'Sistema de {}' ---".format(strAdministrador))
    print("1. CRUD Empleado")
    print("2. CRUD Cargo")
    print("3. CRUD Departamento")
    print("4. CRUD Area")
    print("5. CRUD Sexo")
    print("6. CRUD CargaFamiliar")
    print("7. CRUD Relacion")
    print("8. CRUD ContactoEmergencia")
    print("8. CRUD Credenciales")
    print("9. Salir")
    op = int(input())
    if op == 1:
        print("No disponible")
    if op == 2:
        print("No disponible")
    if op == 3:
        print("No disponible")
    if op == 4:
        print("No disponible")
    if op == 5:
        print("No disponible")
    if op == 6:
        print("No disponible")
    if op == 7:
        print("No disponible")
    if op == 8:
        print("No disponible")
    if op == 9:
        repetir = False
    return False

# Ejecucion del menu
def iniciarMenu():
    while (menuPrincipal()):
        pass
