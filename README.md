# EV4-TallerDeDesarrolloDeAplicaciones
Listado de empleados  

## Flujo
El programa principal es `Principal.py`.  

## Imports
Principal.py  

 - sql_conn.py  
	 - Para las comunicaciones con la base de datos  
 - sitioRecursosHumanos  
	 - Para el menú de Recursos Humanos  
 - sitioEmpleado  
	 - Para el menú de Empleado  
 - sitioJefe  
	 - Para el menú de Jefe  
 - sitioAdministrador  
	 - Para el menú de Administrador  

## Archivos
### Principal.py  
 - Es el programa principal  
 - Sobre la Base de Datos  
	 - Llama a abrir la conexión  
	 - Llama a crear las tablas  
Contiene el menú que hace las llamadas a los otros archivos `.py` mediante los `imports`.  

---
### sitioRecursosHumanos.py
 - Contiene el menú para el usuario de recursos humanos  
 - Tiene funciones típicas CRUD:  
	 - Listar Empleados  
		 - Genera una lista de todos los empleados en la base de datos  
	 - Agregar Empleado  
		 - Permite agregar un empleado a la base de datos.  
	 - Buscar Empleado  
		 - Permite la búsqueda de un empleado  
		 - Filtros:  
			 - Por sexo  
			 - Por Área  
			 - Por RUT  
	 - Eliminar Empleado  
		 - Permite eliminar un empleado por su RUT  
	 - Modificar Empleado  
		 - Permite modificar los datos de un empleado buscándolo por su RUT.  

---
### ...