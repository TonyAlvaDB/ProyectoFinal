import mysql.connector


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
            ("No existe conexion que cerrar")

    
    def crearBaseDeDatos(self, nombre):
        """
        Esta funcion se encarga de crear la base de datos
        
        Solo se usara esta funcion una vez para crear una sola base de datos. Se puede ingresar una nueva 
        base de datos de ser necesario, pero lo normal seria hacerla una sola vez a la hora de ingresar por
        primera vez a la aplicacion.
        
        Returns:
        None
        """
        self.myCursor.execute(f'CREATE DATABASE {nombre}')
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
        self.myCursor.execute(f'CREATE TABLE {nombre} (id INT AUTO_INCREMENT PRIMARY KEY, Producto VARCHAR(255), Precio VARCHAR(255), Cantidad VARCHAR(255))')
        print(f'Tabla {nombre} creada correctamente')
        
    
    def ingresarDatos(self, nombre, precio, cantidad, tabla):
        """ 
        Esta funcion se encarga de ingresar los datos a la tabla
        
        Estan pendientes las autentificaciones de producto para verificar si x producto esta dentro de la base
        para solo incrementar la cantidad o crear una linea nueva
        
        Returns:
        None
        """
        
        self.myCursor.execute(f'INSERT INTO {tabla} (Producto, Precio, Cantidad) VALUES ({nombre}, {precio}, {cantidad})')
        self.conexion.commit()
        print(f"El producto {nombre} ha sido ingresado correctamente. Este se inserto en la fila {self.myCursor.lastrowid}")
        
        
    def eliminarDatos(self, datoParaBuscar, auxuliarParaEliminar, tabla):
        """ 
        Esta funcion se encargara de eliminar un dato dado por parametro
        
        Esta funcion debe recibir un dato que deseemos eliminar, la tabla 
        
        Returns:
        None
        """
        
        self.myCursor.execute(f'DELETE FROM {tabla} WHERE {auxuliarParaEliminar} = "{datoParaBuscar}"')
        print("Datos eliminados correctamente")
        
    def seleccionarTodosLosDatos(self, tabla):
        """ 
        Esta funcion selecciona todos los datos de una tabla.
        
        Para poder ver los datos se tiene que iterar con un for en lo que retorna esta funcion
        
        Returns:
        Lista
        """
        self.myCursor.execute(f'SELECT * FROM {tabla}')
        myresult = self.myCursor.fetchall()
        return myresult
        
    
    
        