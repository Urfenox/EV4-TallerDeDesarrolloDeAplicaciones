import os
import sql_conn
import sitioRecursosHumanos
import sitioEmpleado
import sitioJefe
import sitioAdministrador

os.system("cls")

# Conexion
sql_conn.abrirConn()
# Crea las tablas
sql_conn.crearTablas()

# Menu principal
def menuPrincipal():
    repetir = True
    print("\n --- Bienvenido al 'Listado de Usuarios' ---")
    print("1. Soy Recursos Humanos")
    print("2. Soy Empleado")
    print("3. Soy Jefe")
    print("4. Soy Administrador")
    print("5. Salir")
    op = int(input())
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
    return False

# Ejecucion del menu
def menuPrincipal():
    while (menuPrincipal()):
        pass
menuPrincipal()