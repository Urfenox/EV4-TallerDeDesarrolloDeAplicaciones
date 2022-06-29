import CRUD_Empleados
import Utilidades



def menuPrincipal():
    Utilidades.limpiarConsola()
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
        CRUD_Empleados.Explorar()
    if op == 2:
        CRUD_Empleados.Crear()
    if op == 3:
        CRUD_Empleados.Explorar()
    if op == 4:
        CRUD_Empleados.Remover()
    if op == 5:
        CRUD_Empleados.Actualizar()
    if op == 6:
        repetir = False
    return False

# Ejecucion del menu principal (solo accesible desde inicioSesion())
def iniciarMenu():
    while (menuPrincipal()):
        pass

def inicioSesion():
    clave = input("Ingrese Clave de Recursos Humanos: ")
    if (clave == Utilidades.claveRRHH):
        iniciarMenu()
    
# Ejecucion del menu de inicio de sesion (solo accesible desde RecursosHumanos())
def menuInicioSesion():
    while (inicioSesion()):
        pass

def RecursosHumanos():
    Utilidades.limpiarConsola()
    repetir = True
    print("\n --- Bienvenido a 'Recursos Humanos' ---")
    print("1. Iniciar Sesion")
    print("2. Salir")
    op = int(input())
    if op == 1:
        menuInicioSesion()
    if op == 2:
        repetir = False
    return False

# Ejecucion del menu inicial (accesible solo por llamada externa)
def menuRecursosHumanos():
    while (RecursosHumanos()):
        pass
