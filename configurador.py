import os
import sys
import time
import sql_conn
import Utilidades
import CRUD_Area
import CRUD_Departamento
import CRUD_Cargo
import CRUD_Sexo
import CRUD_Relacion



# Solo se llama al iniciar el programa
def iniciador():
    if (os.path.exists("myDB.db") == False):
        # El programa se debe configurar
        # Crear conexion
        sql_conn.abrirConn()
        # Iniciar Base de Datos
        sql_conn.iniciarDB()
        primerInicio()

def mostrarEULA():
    Utilidades.limpiarConsola()
    print("Por favor tomese su tiempo para leer nuestro EULA.\n\n")
    time.sleep(5) # Pausar por 5 segundos.
    f = open("eula.txt", "r")
    print(f.read())
    time.sleep(10) # 10 sec para dar tiempo de leer
    print("\n\n¿Acepta nuestro 'EULA'? \n    1. Si\n    2. No")
    time.sleep(3) # 3 sec para asegurarse que el usuario no ingrese una opcion muy rapido
    op = int(input("Ingrese su opcion: "))
    if op == 1:
        return True
    else:
        return False

def AñadirDatosIniciales():
    # INGRESO DATOS AREA
    print("Ahora vamos a generar datos en la tabla 'Area'.")
    continuar = True
    while continuar:
        CRUD_Area.Agregar(input("Ingrese el nombre del 'Area': "))
        print("¿Ingresar nueva Area?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
    # INGRESO DATOS DEPARTAMENTO
    print("Ahora vamos a generar datos en la tabla 'Departamento'.")
    continuar = True
    while continuar:
        CRUD_Departamento.Agregar(input("Ingrese el nombre del 'Departamento': "), int(input("Ingrese el vinculo con 'Area': ")))
        print("¿Ingresar nuevo 'Departamento'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
    # INGRESO DATOS CARGO
    print("Ahora vamos a generar datos en la tabla 'Cargo'.")
    continuar = True
    while continuar:
        CRUD_Cargo.Agregar(input("Ingrese el nombre del 'Cargo': "), int(input("Ingrese el vinculo con 'Departamento': ")))
        print("¿Ingresar nuevo 'Cargo'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
    Utilidades.limpiarConsola()
    # INGRESO DATOS SEXO
    print("Ahora vamos a generar datos en la tabla 'Sexo'.")
    continuar = True
    while continuar:
        CRUD_Sexo.Agregar(input("Ingrese el nombre del 'Sexo': "))
        print("¿Ingresar nuevo 'Sexo'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
    Utilidades.limpiarConsola()
    # INGRESO DATOS RELACION
    print("Ahora vamos a generar datos en la tabla 'Relacion'.")
    continuar = True
    while continuar:
        CRUD_Relacion.Agregar(input("Ingrese el nombre de la 'Relacion': "))
        print("¿Ingresar nueva 'Relacion'?\n    1. Si\n    2. No")
        op = int(input("Ingrese la opcion: "))
        if (op == 2):
            continuar = False
    Utilidades.limpiarConsola()
    sql_conn.conn.commit()



# Esta funcion solo se llama cuando el programa es iniciado por primera vez.
def primerInicio():
    Utilidades.limpiarConsola()
    print("Este es el primer inicio de este programa.")
    print("En esta etapa:")
    print("    - Ingresara datos basicos para el funcionamiento de la Base de Datos.")
    print("    - Se le indicaran las claves para ciertas operaciones y cuentas.")
    print("Esta etapa solo se inicia al iniciar el programa por primera ves.")
    time.sleep(5)
    if (mostrarEULA() == False):
        Utilidades.limpiarConsola()
        print("No puede usar este programa si no acepta nuestro EULA.")
        time.sleep(3)
        Utilidades.eliminarBaseDeDatos(True) # Elimina la base de datos (ya que esta vacia).
        #   Asi la proxima puede volver a configurar.
        sys.exit() # Cierra el programa.
    else:
        Utilidades.limpiarConsola()
        print("Este programa debe ser configurado por ser la primera vez que inicia.")
        time.sleep(4)
        Utilidades.limpiarConsola()
        AñadirDatosIniciales()
        print("Ya casi terminamos. Ahora le daremos las contraseñas de fabrica.\n    Anotelas en algun lugar, sin estas no podra realizar ciertas operaciones.\n\n")
        time.sleep(3)
        print("    Clave 'Administrador': {}".format(Utilidades.claveAdmin))
        print("    Clave 'Recursos Humanos': {}".format(Utilidades.claveRRHH))
        time.sleep(5)
        input("Presione 'Enter' para continuar...")
