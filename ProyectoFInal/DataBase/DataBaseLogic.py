import mysql.connector


class BaseDeDatos:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexion = None   
        self.myCursor = self.conexion.cursor()


    def conectarLaBaseDeDatos(self):
        self.conexion = mysql.connector.connect(
            host = self.host, 
            user = self.user,
            password = self.password,
            database = self.database
        )
        
        if self.conexion.is_connected():
            #Todos los print los tenemos que cambiar por alertas en pantalla. Tambien tenemos que hacer 
            #que los datos entren por pantalla. Podriamos poner usuario y contrasenia para entrar
            #y usar eso para ingresar a la base de datos.
            print("La conexion a la base de datos ha sido exitosa")
        else:
            print("Error en la conexion")
            
    def crearBaseDeDatos(self, nombre):
        #Tenemos que autentificar si la base de datos ya estaba creada antes de crearla.
        #Esto lo vamos a hacer en una lista que sera global.
        self.myCursor.execute(f'CREATE DATABASE {nombre}')
        print("Base de datos creada correctamente")
        
        
    def desconectar(self):
        if self.conexion.is_connected():
            self.conexion.close()
            print("La conexion ha sido detenida")
        else:
            ("No existe conexion que cerrar")
    
    
    def ingresarDatos(self, nombre, cantidad, precio):