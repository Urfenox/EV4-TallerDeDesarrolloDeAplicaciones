import os
import sql_conn

# Este script se encarga de realiar las operaciones basicas CRUD para la tabla 'Empleado'.

# aqui podria ser para las cosas de copias de seguridad...

def Agregar(RUT, NombresApelidos, num_Sexo, direccion, telefono, num_Cargo, fechaIngreso, num_Contacto):
    sql_conn.miCursor.execute("INSERT INTO EMPLEADO VALUES (?, ?, ?, ?, ?, ?, ?, ?);", (RUT, NombresApelidos, num_Sexo, direccion, telefono, num_Cargo, fechaIngreso, num_Contacto))
    print("\n Empleado '{}: {}' agregado \n".format(RUT, NombresApelidos))

def Modificar():
    print("No disponible")

def Eliminar():
    print("No disponible")

def Obtener():
    print("No disponible")
