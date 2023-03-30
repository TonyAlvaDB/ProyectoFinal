import mysql.connector


class BaseDeDatos:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexion = None
        
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
            
    def desconectar(self):
        if self.conexion.is_connected():
            self.conexion.close()
            print("La conexion ha sido detenida")
        else:
            ("No existe conexion que cerrar")
    
    
    def __init__(self):
        self.conectar()