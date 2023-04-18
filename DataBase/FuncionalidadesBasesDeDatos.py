from DataBase.DataBaseLogic import BaseDeDatos


class PantallaCrearTabla(BaseDeDatos):
    def __init__(self, host, user, password, database, tabla) -> None:
        super().__init__(host, user, password, database)
        self.tabla = tabla

    def crearTabla(self):
        # Método para crear una tabla en la base de datos
        self.conectarLaBaseDeDatos()
        self.crearTablaNueva(self.tabla)
        self.desconectar()
        
        
        



