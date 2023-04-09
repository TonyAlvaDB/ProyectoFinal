from PyQt6 import QtCore, QtGui, QtWidgets
from UI.qtMainWindow import Ui_qtMainWindow
from Application.Funcion.moduloFuncion import *


class FrmMain(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_qtMainWindow()
        self.ui.setupUi(self)
        self.ui.qtBTNCreacionDeBodegas.clicked.connect(self.onClickqtBTNCreacionDeBodegas)
        self.ui.qtBTNModificaInventarios.clicked.connect(self.onClickqtBTNModificarInventarios)
        self.ui.qtBTNRegistroDeArticulos.clicked.connect(self.onClickqtBTNRegistroDeArticulos)
        self.ui.qtBTNGestionDeBodegas.clicked.connect(self.onClickqtBTNGestionDeBodegas)
        self.ui.qtMNUSalir.triggered.connect(self.onClickqtMNUSalir)
        self.pantalla1 = None
        self.pantalla2 = None
        
        
    def onClickqtBTNCreacionDeBodegas(self):
        self.pantalla1 = CreacionBodega()
        self.pantalla1.show()
        
    def onClickqtBTNModificarInventarios(self):
        self.pantalla2 = ModificarInventarios()
        self.pantalla2.show()    

    def onClickqtBTNRegistroDeArticulos(self):
        self.pantalla2 = RegistroArticulos()
        self.pantalla2.show() 

    def onClickqtBTNGestionDeBodegas(self):
        self.pantalla2 = GestionBodegas()
        self.pantalla2.show() 

    def onClickqtMNUSalir(self):
        quit()