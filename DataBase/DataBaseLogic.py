import mysql.connector


class BaseDeDatos:
    def __init__(self, host, user, password, database) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexion = None   
        self.myCursor = None

    
    def conectarLaBaseDeDatos(self, host, user, password, database):
        # Método para establecer la conexión con la base de datos
        self.conexion = mysql.connector.connect(
            host=host, 
            user=user,
            password=password,
            database=database
        )
        if self.conexion.is_connected():
            print("La conexión a la base de datos ha sido exitosa")
            self.myCursor = self.conexion.cursor()
        else:
            print("Error en la conexión")
            
    def desconectar(self):
        # Método para cerrar la conexión con la base de datos
        if self.conexion.is_connected():
            self.myCursor.close()
            self.conexion.close()
            print("La conexión ha sido detenida")
        else:
            print("No existe conexión que cerrar")

    def crearBaseDeDatos(self, nombre):
        # Método para crear una nueva base de datos
        self.myCursor.execute(f'CREATE DATABASE {nombre}')
        print("Base de datos creada correctamente")

    def crearTablaNueva(self, nombre):
        # Método para crear una nueva tabla en la base de datos
        self.myCursor.execute(f'CREATE TABLE {nombre} (id INT AUTO_INCREMENT PRIMARY KEY, Producto VARCHAR(255), Precio VARCHAR(255), Cantidad VARCHAR(255))')
        print(f'Tabla {nombre} creada correctamente')

    def ingresarDatos(self, nombre, precio, cantidad, tabla):
        # Método para ingresar datos a una tabla en la base de datos
        query = 'INSERT INTO {} (Producto, Precio, Cantidad) VALUES (%s, %s, %s)'.format(tabla)
        values = (nombre, precio, cantidad)
        self.myCursor.execute(query, values)
        self.conexion.commit()
        print(f"El producto {nombre} ha sido ingresado correctamente. Este se insertó en la fila {self.myCursor.lastrowid}")

    def eliminarDatos(self, datoParaBuscar, auxiliarParaEliminar, tabla):
        # Método para eliminar datos de una tabla en la base de datos
        query = 'DELETE FROM {} WHERE {} = %s'.format(tabla, auxiliarParaEliminar)
        values = (datoParaBuscar,)
        self.myCursor.execute(query, values)
        self.conexion.commit()
        print("Datos eliminados correctamente")

    def seleccionarTodosLosDatos(self, tabla) -> list:
        # Método para seleccionar todos los datos de una tabla en la base de datos
        self.myCursor.execute(f'SELECT * FROM {tabla}')
        myresult = self.myCursor.fetchall()
        return myresult
