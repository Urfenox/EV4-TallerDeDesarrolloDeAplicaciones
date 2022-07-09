import os
import sys
import time
import random
import string
import sql_conn
import Utilidades

os.system("title myEmployeerArray")

def generarStringAleatorio(longitud):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(longitud))
    return result_str

def _eliminarDDB():
    # NO llamar esta funcion JAMAS.
    #    Solo puede ser llamada desde eliminarBaseDeDatos().
    sql_conn.miCursor.close()
    sql_conn.conn.close()
    os.remove("myDB.db")

def eliminarBaseDeDatos(forzar):
    Utilidades.limpiarConsola()
    if (forzar):
        _eliminarDDB()
    else:
        print("-----------------------------------------------------------------------------------")
        print(" ---   ¡ESTA ACCION ELIMINARA LA BASE DE DATOS Y TODA SU INFORMACION DENTRO!   --- ")
        print(" --- PARA REALIZAR ESTA OPERACION ES NECESARIO TENER LA CLAVE DE ADMINISTRADOR --- ")
        print("-----------------------------------------------------------------------------------")
        clave = input("Ingrese la clave de administrador: ")
        if (clave == claveAdmin):
            _eliminarDDB()

def pausarContinuar():
    input("Presione 'Enter' para continuar...")

def salirPrograma():
    limpiarConsola()
    print("Cerrando...")
    time.sleep(2)
    print("¡No vemos! ;)")
    time.sleep(1)
    sys.exit() # Cierra el programa.
    
def limpiarConsola():
    # Limpia la consola
    os.system("cls")

def Main():
    global claveAdmin
    global claveRRHH
    claveAdmin = "gMokBaD5vrgMdPTP"
    claveRRHH = "eB3xf4Ip"
    
Main()