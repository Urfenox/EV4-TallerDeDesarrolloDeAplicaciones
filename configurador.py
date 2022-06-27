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
    print("Por favor tomese su tiempo para leer nuestro EULA.\n\n")
    f = open("eula.txt", "r")
    print(f.read())
    time.sleep(10) # Pausar por 10 segundos.
    print("\n\n¿Acepta nuestro 'EULA'? \n    1. Si\n    2. No")   
    op = int(input("Ingrese su opcion: "))
    if op == 1:
        return True
    else:
        return False

# Esta funcion solo se llama cuando el programa es iniciado por primera vez.
def primerInicio():
    Utilidades.limpiarConsola()
    if (mostrarEULA() == False):
        print("No puede usar este programa si no acepta nuestro EULA.")
        os.remove("myDB.db") # Elimina la base de datos (ya que esta vacia).
        #   Asi la proxima puede volver a configurar.
        sys.exit() # Cierra el programa.
    else:
        print("Este programa debe ser configurado por ser la primera vez que inicia.")
        print("Ahora vamos a generar datos en la tabla 'Area'.")
        continuar = True
        while continuar:
            CRUD_Area.Agregar(input("Ingrese el nombre del 'Area': "))
            op = int(input("¿Ingresar nueva Area?\n    1. Si\n    2. No"))
            if (op == 1):
                continuar = False
        print("Ahora vamos a generar datos en la tabla 'Departamento'.")
        continuar = True
        while continuar:
            CRUD_Departamento.Agregar(input("Ingrese el nombre del 'Departamento': "), int(input("Ingrese el vinculo con 'Area': ")))
            op = int(input("¿Ingresar nuevo 'Departamento'?\n    1. Si\n    2. No"))
            if (op == 1):
                continuar = False
        print("Ahora vamos a generar datos en la tabla 'Cargo'.")
        continuar = True
        while continuar:
            CRUD_Cargo.Agregar(input("Ingrese el nombre del 'Cargo': "), int(input("Ingrese el vinculo con 'Departamento': ")))
            op = int(input("¿Ingresar nuevo 'Cargo'?\n    1. Si\n    2. No"))
            if (op == 1):
                continuar = False
        Utilidades.limpiarConsola()
        print("Ahora vamos a generar datos en la tabla 'Sexo'.")
        continuar = True
        while continuar:
            CRUD_Sexo.Agregar(input("Ingrese el 'Sexo': "))
            op = int(input("¿Ingresar nuevo 'Sexo'?\n    1. Si\n    2. No"))
            if (op == 1):
                continuar = False
        Utilidades.limpiarConsola()
        print("Ahora vamos a generar datos en la tabla 'Relacion'.")
        continuar = True
        while continuar:
            CRUD_Relacion.Agregar(input("Ingrese el nombre de la 'Relacion': "))
            op = int(input("¿Ingresar nueva 'Relacion'?\n    1. Si\n    2. No"))
            if (op == 1):
                continuar = False
        Utilidades.limpiarConsola()
        print("Ya casi terminamos. Ahora le daremos las contraseñas de fabrica.\n    Anotelas en algun lugar, sin estas no podra realizar ciertas operaciones.\n\n")
        print("    Clave 'Administrador': {}".format(Utilidades.claveAdmin))
        print("    Clave 'Recursos Humanos': {}".format(Utilidades.claveRRHH))
