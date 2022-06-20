import sqlite3
conn = None
miCursor = None

# Crea la conexion a la base de datos
def abrirConn():
    conn = sqlite3.connect("myDB.db")
    miCursor = conn.cursor()

# Crea las tablas si estas no existen
def crearTablas():
    miCursor.execute("CREATE TABLE IF NOT EXIST EMPLEADO (RUT Number,NombresApellidos VARCHAR2(70),num_Sexo NUMBER,direccion VARCHAR2(70),telefono VARCHAR2(12),num_Cargo NUMBER,fechaIngreso DATE,num_Contacto NUMBER);")
    miCursor.execute("CREATE TABLE IF NOT EXIST CARGO (codCargo NUMBER,nombreCargo VARCHAR2(30),num_Departamento NUMBER);")
    miCursor.execute("CREATE TABLE IF NOT EXIST DEPARTAMENTO (codDepartamento NUMBER,Nombre VARCHAR2(30),num_Area NUMBER);")
    miCursor.execute("CREATE TABLE IF NOT EXIST AREA (codArea NUMBER,Nombre VARCHAR2(30));")
    miCursor.execute("CREATE TABLE IF NOT EXIST SEXO (codSexo NUMBER,Nombre VARCHAR2(20));")
    miCursor.execute("CREATE TABLE IF NOT EXIST CARGA_FAMILIAR (rut_carga NUMBER,NombresApellidos VARCHAR2(30),num_Empleado NUMBER,num_Relacion NUMBER,num_Sexo NUMBER);")
    miCursor.execute("CREATE TABLE IF NOT EXIST RELACION (codRelacion NUMBER,Nombre VARCHAR2(20));")
    miCursor.execute("CREATE TABLE IF NOT EXIST CONTACTO_EMERGENCIA (codContacto NUMBER,NombreApellido VARCHAR2(30),num_Relacion NUMBER,num_Sexo NUMBER,num_Empleado NUMBER,contacto VARCHAR2(30));")

# Crea las PKs a las tablas
def aplicarConstraintsPKs():
    miCursor.execute("ALTER TABLE EMPLEADO ADD CONSTRAINT PK_EMPLEADO_rut PRIMARY KEY (rut);")
    miCursor.execute("ALTER TABLE CARGO ADD CONSTRAINT PK_CARGO_codCargo PRIMARY KEY (codCargo);")
    miCursor.execute("ALTER TABLE DEPARTAMENTO ADD CONSTRAINT PK_DEPARTAMENTO_codDepartamento PRIMARY KEY (codDepartamento);")
    miCursor.execute("ALTER TABLE AREA ADD CONSTRAINT PK_AREA_codArea PRIMARY KEY (codArea);")
    miCursor.execute("ALTER TABLE SEXO ADD CONSTRAINT PK_SEXO_codSexo PRIMARY KEY (codSexo);")
    miCursor.execute("ALTER TABLE CARGA_FAMILIAR ADD CONSTRAINT PK_CARGA_FAMILIAR_rut_carga PRIMARY KEY (rut_carga);")
    miCursor.execute("ALTER TABLE RELACION ADD CONSTRAINT PK_RELACION_codRelacion PRIMARY KEY (codRelacion);")
    miCursor.execute("ALTER TABLE CONTACTO_EMERGENCIA ADD CONSTRAINT PK_CONTACTO_EMERGENCIA_codContacto PRIMARY KEY (codContacto);")

# Crea las FKs a las tablas
def aplicarConstraintsFKs():
    miCursor.execute("ALTER TABLE EMPLEADO ADD CONSTRAINT FK_EMPLEADO_num_Sexo FOREIGN KEY (num_Sexo) REFERENCES SEXO(codSexo);")
    miCursor.execute("ALTER TABLE EMPLEADO ADD CONSTRAINT FK_EMPLEADO_num_Cargo FOREIGN KEY (num_Cargo) REFERENCES CARGO(codCargo);")
    miCursor.execute("ALTER TABLE EMPLEADO ADD CONSTRAINT FK_EMPLEADO_num_Contacto FOREIGN KEY (num_Contacto) REFERENCES CONTACTO_EMERGENCIA(codContacto);")
    miCursor.execute("ALTER TABLE CARGO ADD CONSTRAINT FK_CARGO_num_Departamento FOREIGN KEY (num_Departamento) REFERENCES DEPARTAMENTO(codDepartamento);")
    miCursor.execute("ALTER TABLE DEPARTAMENTO ADD CONSTRAINT FK_DEPARTAMENTO_num_Area FOREIGN KEY (num_Area) REFERENCES AREA(codArea);")
    miCursor.execute("ALTER TABLE CARGA_FAMILIAR ADD CONSTRAINT FK_CARGA_FAMILIAR_num_Empleado FOREIGN KEY (num_Empleado) REFERENCES EMPLEADO(RUT);")
    miCursor.execute("ALTER TABLE CARGA_FAMILIAR ADD CONSTRAINT FK_CARGA_FAMILIAR_num_Relacion FOREIGN KEY (num_Relacion) REFERENCES RELACION(codRelacion);")
    miCursor.execute("ALTER TABLE CARGA_FAMILIAR ADD CONSTRAINT FK_CARGA_FAMILIAR_num_Sexo FOREIGN KEY (num_Sexo) REFERENCES SEXO(codSexo);")
    miCursor.execute("ALTER TABLE CONTACTO_EMERGENCIA ADD CONSTRAINT FK_CONTACTO_EMERGENCIA_num_Relacion FOREIGN KEY (num_Relacion) REFERENCES RELACION(codRelacion);")
    miCursor.execute("ALTER TABLE CONTACTO_EMERGENCIA ADD CONSTRAINT FK_CONTACTO_EMERGENCIA_num_Sexo FOREIGN KEY (num_Sexo) REFERENCES SEXO(codSexo);")
    miCursor.execute("ALTER TABLE CONTACTO_EMERGENCIA ADD CONSTRAINT FK_CONTACTO_EMERGENCIA_num_Empleado FOREIGN KEY (num_Empleado) REFERENCES EMPLEADO(rut);")

