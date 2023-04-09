
import mysql.connector

"""
La informacion basica de la base de datos es:
Hostname: 127.0.0.1
Port: 3306
Username: root
Password: 22011993Doremi123

"""
class BaseDeDatos:
    def __init__(self, host, user, password, database) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexion = None   
        self.myCursor = self.conexion.cursor()


    def conectarLaBaseDeDatos(self):
        """
        Esta funcion se encarga de la inicializacion de la base de datos
        
        Usa el objeto mismo para poder ingresar a la base de datos. El usuario y la contraseña de la base
        de datos seria la misma que se usa para ingresar a la aplicacion. Se inicializara la base de datos
        cada vez que entremos en la pantalla de cambios de inventario
        
        Returns:
        None
        """
        self.conexion = mysql.connector.connect(
            host = self.host, 
            user = self.user,
            password = self.password,
            database = self.database
        )
        
        if self.conexion.is_connected():
            print("La conexion a la base de datos ha sido exitosa")
        else:
            print("Error en la conexion")
            
    def desconectar(self):
        """ 
        Esta funcion se encarga de cerrar de la base de datos
        
        Usa el objeto mismo para poder cerrar a la base de datos. Se cerrara la base de datos cuando se 
        cierre la pantalla de bodegas.
        
        Returns:
        None
        """
        
        if self.conexion.is_connected():
            self.conexion.close()
            print("La conexion ha sido detenida")
        else:
            print("No existe conexion que cerrar")

    
    def crearBaseDeDatos(self, nombre):
        """
        Esta funcion se encarga de crear la base de datos
        
        Solo se usara esta funcion una vez para crear una sola base de datos. Se puede ingresar una nueva 
        base de datos de ser necesario, pero lo normal seria hacerla una sola vez a la hora de ingresar por
        primera vez a la aplicacion.
        
        Returns:
        None
        """
        
        mySQLFunction = "CREATE DATABASE %s"
        nombreDeBaseDeDatos = nombre
        self.myCursor.execute(mySQLFunction, nombreDeBaseDeDatos)
        print("Base de datos creada correctamente")
        
    def crearTablaNueva(self, nombre):
        """ 
        Esta funcion se encarga de crear tablas
        
        Estas si seran necesarias para guardar los productos. Las bases de datos no seran dinamicas (es decir, 
        no necesitamos poner columnas costumizadas). Al ser una base de datos solo necesitamos tablas que
        nos digan el nombre del producto, el precio y la cantidad que hay.
        
        Returns:
        None
        """
        nombreDeLaTabla = nombre
        mySQLFunction = "CREATE TABLE %s (id INT AUTO_INCREMENT PRIMARY KEY, Producto VARCHAR(255), Precio VARCHAR(255), Cantidad VARCHAR(255))"
        self.myCursor.execute(mySQLFunction, nombre)
        print(f'Tabla {nombre} creada correctamente')
        
    
    def ingresarDatos(self, nombre, precio, cantidad, tabla):
        """ 
        Esta funcion se encarga de ingresar los datos a la tabla
        
        Estan pendientes las autentificaciones de producto para verificar si x producto esta dentro de la base
        para solo incrementar la cantidad o crear una linea nueva
        
        Returns:
        None
        """
        nombreDelProducto = nombre
        cantidadDelProducto = cantidad
        precioDelProducto = precio
        tablaDondeSeInserta = tabla
        mySQLFunction = "INSERT INTO %s (Producto, Precio, Cantidad) VALUES (%s, %s, %s)"
        self.myCursor.execute(mySQLFunction, tablaDondeSeInserta, nombreDelProducto, precioDelProducto, cantidadDelProducto)
        self.conexion.commit()
        print(f"El producto {nombre} ha sido ingresado correctamente. Este se inserto en la fila {self.myCursor.lastrowid}")
        
        
    def eliminarDatos(self, datoParaBuscar, auxuliarParaEliminar, tabla):
        """ 
        Esta funcion se encargara de eliminar un dato dado por parametro
        
        Esta funcion debe recibir un dato que deseemos eliminar, la tabla, y el tipo de dato que se desea buscar.
        Es decir, se tiene que meter tambien si se desea buscar por nombre, o precio, o ID.
        
        Returns:
        None
        """
        datoABuscar = datoParaBuscar
        tipoDeBusqueda = auxuliarParaEliminar
        tablaDondeSeEliminara = tabla
        mySQLFunction = "DELETE FROM %s WHERE %s = '%s'"
        
        self.myCursor.execute(mySQLFunction, tablaDondeSeEliminara, tipoDeBusqueda, datoABuscar)
        print("Datos eliminados correctamente")
        
    def seleccionarTodosLosDatos(self, tabla) -> list:
        """ 
        Esta funcion selecciona todos los datos de una tabla.
        
        Para poder ver los datos se tiene que iterar con un for en lo que retorna esta funcion
        
        Returns:
        Lista
        """
        tablaParaRetornar = tabla
        mySQLFunction = "SELECT * FROM %s"
        self.myCursor.execute(mySQLFunction, tablaParaRetornar)
        myresult = self.myCursor.fetchall()
        return myresult
        
    
    
    
        