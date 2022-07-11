import CRUD_Sexo
import CRUD_Area
import CRUD_Cargo
import CRUD_Relacion
import CRUD_Empleados
import CRUD_Credenciales
import CRUD_Departamento
import CRUD_CargaFamiliar
import CRUD_ContactoEmergencia
import Utilidades
# Cambia el directorio de trabajo
#   = current file path
import os
from os.path import abspath, dirname
os.chdir(dirname(abspath(__file__)))



def C_Empleado():
    continuar = True
    while continuar:
        CRUD_Empleados.Crear()
        print("¿Ingresar nuevo 'Empleado'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def R_Empleado():
    continuar = True
    while continuar:
        CRUD_Empleados.Explorar()
        print("Buscar/Listar 'Empleado'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def U_Empleado():
    continuar = True
    while continuar:
        CRUD_Empleados.Actualizar()
        print("Modificar 'Empleado'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def D_Empleado():
    continuar = True
    while continuar:
        CRUD_Empleados.Remover()
        print("Eliminar 'Empleado'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def menuEmpleado():
    print(" --- CRUD Empleado --- ")
    print("    1. Agregar")
    print("    2. Buscar/Listar")
    print("    3. Actualizar")
    print("    4. Eliminar")
    op = int(input("Ingrese su opcion: "))
    if (op == 1):
        C_Empleado()
        Utilidades.pausarContinuar()
    elif (op == 2):
        R_Empleado()
        Utilidades.pausarContinuar()
    elif (op == 3):
        U_Empleado()
        Utilidades.pausarContinuar()
    elif (op == 4):
        D_Empleado()
        Utilidades.pausarContinuar()

def C_Cargo():
    continuar = True
    while continuar:
        CRUD_Cargo.Crear()
        print("¿Ingresar nuevo 'Cargo'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def R_Cargo():
    continuar = True
    while continuar:
        CRUD_Cargo.Explorar()
        print("Buscar/Listar 'Cargo'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def U_Cargo():
    continuar = True
    while continuar:
        CRUD_Cargo.Actualizar()
        print("Modificar 'Cargo'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def D_Cargo():
    continuar = True
    while continuar:
        CRUD_Cargo.Remover()
        print("Eliminar 'Cargo'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def menuCargo():
    print(" --- CRUD Cargo --- ")
    print("    1. Agregar")
    print("    2. Buscar/Listar")
    print("    3. Actualizar")
    print("    4. Eliminar")
    op = int(input("Ingrese su opcion: "))
    if (op == 1):
        C_Cargo()
        Utilidades.pausarContinuar()
    elif (op == 2):
        R_Cargo()
        Utilidades.pausarContinuar()
    elif (op == 3):
        U_Cargo()
        Utilidades.pausarContinuar()
    elif (op == 4):
        D_Cargo()
        Utilidades.pausarContinuar()

def C_Departamento():
    continuar = True
    while continuar:
        CRUD_Departamento.Crear()
        print("¿Ingresar nuevo 'Departamento'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def R_Departamento():
    continuar = True
    while continuar:
        CRUD_Departamento.Explorar()
        print("Buscar/Listar 'Departamento'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def U_Departamento():
    continuar = True
    while continuar:
        CRUD_Departamento.Actualizar()
        print("Modificar 'Departamento'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def D_Departamento():
    continuar = True
    while continuar:
        CRUD_Departamento.Remover()
        print("Eliminar 'Departamento'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def menuDepartamento():
    print(" --- CRUD Departamento --- ")
    print("    1. Agregar")
    print("    2. Buscar/Listar")
    print("    3. Actualizar")
    print("    4. Eliminar")
    op = int(input("Ingrese su opcion: "))
    if (op == 1):
        C_Departamento()
        Utilidades.pausarContinuar()
    elif (op == 2):
        R_Departamento()
        Utilidades.pausarContinuar()
    elif (op == 3):
        U_Departamento()
        Utilidades.pausarContinuar()
    elif (op == 4):
        D_Departamento()
        Utilidades.pausarContinuar()

def C_Area():
    continuar = True
    while continuar:
        CRUD_Area.Crear()
        print("¿Ingresar nuevo 'Area'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def R_Area():
    continuar = True
    while continuar:
        CRUD_Area.Explorar()
        print("Buscar/Listar 'Area'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def U_Area():
    continuar = True
    while continuar:
        CRUD_Area.Actualizar()
        print("Modificar 'Area'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def D_Area():
    continuar = True
    while continuar:
        CRUD_Area.Remover()
        print("Eliminar 'Area'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def menuArea():
    print(" --- CRUD Area --- ")
    print("    1. Agregar")
    print("    2. Buscar/Listar")
    print("    3. Actualizar")
    print("    4. Eliminar")
    op = int(input("Ingrese su opcion: "))
    if (op == 1):
        C_Area()
        Utilidades.pausarContinuar()
    elif (op == 2):
        R_Area()
        Utilidades.pausarContinuar()
    elif (op == 3):
        U_Area()
        Utilidades.pausarContinuar()
    elif (op == 4):
        D_Area()
        Utilidades.pausarContinuar()

def C_Sexo():
    continuar = True
    while continuar:
        CRUD_Sexo.Crear()
        print("¿Ingresar nuevo 'Sexo'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def R_Sexo():
    continuar = True
    while continuar:
        CRUD_Sexo.Explorar()
        print("Buscar/Listar 'Sexo'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def U_Sexo():
    continuar = True
    while continuar:
        CRUD_Sexo.Actualizar()
        print("Modificar 'Sexo'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def D_Sexo():
    continuar = True
    while continuar:
        CRUD_Sexo.Remover()
        print("Eliminar 'Sexo'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def menuSexo():
    print(" --- CRUD Sexo --- ")
    print("    1. Agregar")
    print("    2. Buscar/Listar")
    print("    3. Actualizar")
    print("    4. Eliminar")
    op = int(input("Ingrese su opcion: "))
    if (op == 1):
        C_Sexo()
        Utilidades.pausarContinuar()
    elif (op == 2):
        R_Sexo()
        Utilidades.pausarContinuar()
    elif (op == 3):
        U_Sexo()
        Utilidades.pausarContinuar()
    elif (op == 4):
        D_Sexo()
        Utilidades.pausarContinuar()

def C_CargaFamiliar():
    continuar = True
    while continuar:
        CRUD_CargaFamiliar.Crear()
        print("¿Ingresar nuevo 'CargaFamiliar'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def R_CargaFamiliar():
    continuar = True
    while continuar:
        CRUD_CargaFamiliar.Explorar()
        print("Buscar/Listar 'CargaFamiliar'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def U_CargaFamiliar():
    continuar = True
    while continuar:
        CRUD_CargaFamiliar.Actualizar()
        print("Modificar 'CargaFamiliar'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def D_CargaFamiliar():
    continuar = True
    while continuar:
        CRUD_CargaFamiliar.Remover()
        print("Eliminar 'CargaFamiliar'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def menuCargaFamiliar():
    print(" --- CRUD CargaFamiliar --- ")
    print("    1. Agregar")
    print("    2. Buscar/Listar")
    print("    3. Actualizar")
    print("    4. Eliminar")
    op = int(input("Ingrese su opcion: "))
    if (op == 1):
        C_CargaFamiliar()
        Utilidades.pausarContinuar()
    elif (op == 2):
        R_CargaFamiliar()
        Utilidades.pausarContinuar()
    elif (op == 3):
        U_CargaFamiliar()
        Utilidades.pausarContinuar()
    elif (op == 4):
        D_CargaFamiliar()
        Utilidades.pausarContinuar()

def C_Relacion():
    continuar = True
    while continuar:
        CRUD_Relacion.Crear()
        print("¿Ingresar nuevo 'Relacion'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def R_Relacion():
    continuar = True
    while continuar:
        CRUD_Relacion.Explorar()
        print("Buscar/Listar 'Relacion'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def U_Relacion():
    continuar = True
    while continuar:
        CRUD_Relacion.Actualizar()
        print("Modificar 'Relacion'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def D_Relacion():
    continuar = True
    while continuar:
        CRUD_Relacion.Remover()
        print("Eliminar 'Relacion'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def menuRelacion():
    print(" --- CRUD Relacion --- ")
    print("    1. Agregar")
    print("    2. Buscar/Listar")
    print("    3. Actualizar")
    print("    4. Eliminar")
    op = int(input("Ingrese su opcion: "))
    if (op == 1):
        C_Relacion()
        Utilidades.pausarContinuar()
    elif (op == 2):
        R_Relacion()
        Utilidades.pausarContinuar()
    elif (op == 3):
        U_Relacion()
        Utilidades.pausarContinuar()
    elif (op == 4):
        D_Relacion()
        Utilidades.pausarContinuar()

def C_ContactoEmergencia():
    continuar = True
    while continuar:
        CRUD_ContactoEmergencia.Crear()
        print("¿Ingresar nuevo 'ContactoEmergencia'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def R_ContactoEmergencia():
    continuar = True
    while continuar:
        CRUD_ContactoEmergencia.Explorar()
        print("Buscar/Listar 'ContactoEmergencia'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def U_ContactoEmergencia():
    continuar = True
    while continuar:
        CRUD_ContactoEmergencia.Actualizar()
        print("Modificar 'ContactoEmergencia'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def D_ContactoEmergencia():
    continuar = True
    while continuar:
        CRUD_ContactoEmergencia.Remover()
        print("Eliminar 'ContactoEmergencia'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def menuContactoEmergencia():
    print(" --- CRUD ContactoEmergencia --- ")
    print("    1. Agregar")
    print("    2. Buscar/Listar")
    print("    3. Actualizar")
    print("    4. Eliminar")
    op = int(input("Ingrese su opcion: "))
    if (op == 1):
        C_ContactoEmergencia()
        Utilidades.pausarContinuar()
    elif (op == 2):
        R_ContactoEmergencia()
        Utilidades.pausarContinuar()
    elif (op == 3):
        U_ContactoEmergencia()
        Utilidades.pausarContinuar()
    elif (op == 4):
        D_ContactoEmergencia()
        Utilidades.pausarContinuar()

def C_Credenciales():
    continuar = True
    while continuar:
        CRUD_Credenciales.Crear()
        print("¿Ingresar nuevo 'Credenciales'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def R_Credenciales():
    continuar = True
    while continuar:
        CRUD_Credenciales.Explorar()
        print("Buscar/Listar 'Credenciales'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def U_Credenciales():
    continuar = True
    while continuar:
        CRUD_Credenciales.Actualizar()
        print("Modificar 'Credenciales'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def D_Credenciales():
    continuar = True
    while continuar:
        CRUD_Credenciales.Remover()
        print("Eliminar 'Credenciales'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
def menuCredenciales():
    print(" --- CRUD Credenciales --- ")
    print("    1. Agregar")
    print("    2. Buscar/Listar")
    print("    3. Actualizar")
    print("    4. Eliminar")
    op = int(input("Ingrese su opcion: "))
    if (op == 1):
        C_Credenciales()
        Utilidades.pausarContinuar()
    elif (op == 2):
        R_Credenciales()
        Utilidades.pausarContinuar()
    elif (op == 3):
        U_Credenciales()
        Utilidades.pausarContinuar()
    elif (op == 4):
        D_Credenciales()
        Utilidades.pausarContinuar()

def menuPrincipal():
    repetir = True
    print("\n --- Bienvenido al 'Sistema de Administrador' --- ")
    print("1. CRUD Empleado")
    print("2. CRUD Cargo")
    print("3. CRUD Departamento")
    print("4. CRUD Area")
    print("5. CRUD Sexo")
    print("6. CRUD CargaFamiliar")
    print("7. CRUD Relacion")
    print("8. CRUD ContactoEmergencia")
    print("9. CRUD Credenciales")
    print("10. Salir")
    op = int(input())
    if op == 1:
        menuEmpleado()
    if op == 2:
        menuCargo()
    if op == 3:
        menuDepartamento()
    if op == 4:
        menuArea()
    if op == 5:
        menuSexo()
    if op == 6:
        menuCargaFamiliar()
    if op == 7:
        menuRelacion()
    if op == 8:
        menuContactoEmergencia()
    if op == 9:
        menuCredenciales()
    if op == 10:
        repetir = False
    return repetir

# Ejecucion del menu
def iniciarMenu():
    while (menuPrincipal()):
        pass

def iniciarSesion():
    clave = input("Ingrese Clave de Administrador: ")
    if (clave == Utilidades.claveAdmin):
        iniciarMenu()

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
    return repetir

# Ejecucion del menu inicial (accesible solo por llamada externa)
def menuAdministrador():
    while (Administrador()):
        pass
