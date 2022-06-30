r"""Encargado de manejar las conexiones y brindar las variables para codigo que lo requiera.

Esto hace:
  - Crea la conexion a la base de datos con la variable global 'conn'.
  - Crea un cursor para manejar la base de datos con la variable global 'miCursor'.
  - Crea las tablas.
    - Crea las tablas.
    - Crea las PKs.
    - Crea las FKs.

Es importante que ninguna otra variable haga lo mismo que lo que se hace aqui.
"""

#'
import sqlite3

# Crea la conexion a la base de datos
def abrirConn():
    global conn
    global miCursor
    conn = sqlite3.connect("myDB.db")
    miCursor = conn.cursor()

# Inicializa la Base de Datos
def iniciarDB():
    crearTablas()

# Crea las tablas si estas no existen
#   + crea las PKs
#   + crea las FKs
def crearTablas():
    miCursor.execute("CREATE TABLE IF NOT EXISTS EMPLEADO (rut NUMBER PRIMARY KEY,NombreApellidos VARCHAR2(70),num_Sexo NUMBER,direccion VARCHAR2(70),telefono VARCHAR2(12),num_Cargo NUMBER,fechaIngreso DATE,FOREIGN KEY (num_Sexo) REFERENCES SEXO(codSexo));")
    miCursor.execute("CREATE TABLE IF NOT EXISTS CARGO (codCargo NUMBER PRIMARY KEY,nombreCargo VARCHAR2(30),num_Departamento NUMBER,FOREIGN KEY (num_Departamento) REFERENCES DEPARTAMENTO(codDepartamento));")
    miCursor.execute("CREATE TABLE IF NOT EXISTS DEPARTAMENTO (codDepartamento NUMBER PRIMARY KEY,Nombre VARCHAR2(30),num_Area NUMBER,FOREIGN KEY (num_Area) REFERENCES AREA(codArea));")
    miCursor.execute("CREATE TABLE IF NOT EXISTS AREA (codArea NUMBER PRIMARY KEY,Nombre VARCHAR2(30));")
    miCursor.execute("CREATE TABLE IF NOT EXISTS SEXO (codSexo NUMBER PRIMARY KEY,Nombre VARCHAR2(20));")
    miCursor.execute("CREATE TABLE IF NOT EXISTS CARGA_FAMILIAR (rut_carga NUMBER PRIMARY KEY,NombresApellidos VARCHAR2(30),num_Empleado NUMBER,num_Relacion NUMBER,num_Sexo NUMBER,FOREIGN KEY (num_Empleado) REFERENCES EMPLEADO(rut),FOREIGN KEY (num_Relacion) REFERENCES RELACION(codRelacion),FOREIGN KEY (num_Sexo) REFERENCES SEXO(codSexo));")
    miCursor.execute("CREATE TABLE IF NOT EXISTS RELACION (codRelacion NUMBER PRIMARY KEY,Nombre VARCHAR2(20));")
    miCursor.execute("CREATE TABLE IF NOT EXISTS CONTACTO_EMERGENCIA (codContacto NUMBER PRIMARY KEY,NombreApellido VARCHAR2(30),num_Relacion NUMBER,num_Sexo NUMBER,num_Empleado NUMBER,contacto VARCHAR2(30),FOREIGN KEY (num_Relacion) REFERENCES RELACION(codRelacion),FOREIGN KEY (num_Sexo) REFERENCES SEXO(codSexo),FOREIGN KEY (num_Empleado) REFERENCES EMPLEADO(rut));")
    miCursor.execute("CREATE TABLE IF NOT EXISTS CREDENCIAL (codCredencial NUMBER PRIMARY KEY,IDENT NUMBER,Usuario VARCHAR2(20),Clave VARCHAR2(70));")
