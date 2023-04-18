import traceback
from  PyQt6 import QtCore,QtGui,QtWidgets
from UI.qtMainWindow import Ui_qtMainWindow
from UI.qtWDWAgregarBodega import Ui_qtWDWAgregarBodega
from UI.qtWDWControlDeBodegas import Ui_qtWDWControlDeBodegas
from UI.qtWDWInventarios import Ui_qtWDWInventarios
from UI.qtWDWRegistroDeArticulos import Ui_qtWDWRegistroDeArticulos
from Application.Core.moduloCore import *
from DataBase.DataBaseLogic import FileManager as DB


class CreacionBodega(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_qtWDWAgregarBodega() #La propieda ui contiene la instancia de la interfaz grafica que dibujamos
        self.ui.setupUi(self) #Esta linea dibuja la interfaz grafica

        self.ui.qtBTNlimpiar.clicked.connect(self.qtBTNlimpiar_clicked)
        self.ui.qtBTNAgregarBodega.clicked.connect(self.qtBTNAgregarBodega_clicked)

    def qtBTNlimpiar_clicked(self):
        self.ui.qtTXTNombreDeBodega.clear() 
        
    def qtBTNAgregarBodega_clicked(self):
        db = DB('C:\\Users\\aalva\\Progra\\Clone Proyecto final\\ProyectoFinal\\BaseDeDatos')
        if self.ui.qtTXTNombreDeBodega.text() == "":
            QtWidgets.QMessageBox.warning(self, "Error", "Los campos no pueden estar vacíos")
        else:
            nombreTabla = self.ui.qtTXTNombreDeBodega.text()
            columnas = ['id', 'nombre', 'precio', 'cantidad']
            db.create_table(nombreTabla, columnas)
            self.ui.qtTXTNombreDeBodega.clear()
            

class ModificarInventarios(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_qtWDWInventarios()
        self.ui.setupUi(self)


class RegistroArticulos(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_qtWDWRegistroDeArticulos()
        self.ui.setupUi(self)
        self.contador = 1

        reg_ex = QtCore.QRegularExpression("^[0-9]*(\.[0-9]{1,2})?$")
        input_validator = QtGui.QRegularExpressionValidator(reg_ex, self.ui.qtTXTPrecio)
        self.ui.qtTXTPrecio.setValidator(input_validator)
        
        self.ui.qtBTNLimpiar.clicked.connect(self.qtBTNLimpiar_clicked)
        self.ui.qtBTNAgregarArticulo.clicked.connect(self.qtBTNAgregarArticulo)
        self.ui.qtTXTBodega.setText("CDP")
 
    def qtBTNLimpiar_clicked(self):
        self.ui.qtTXTNombre.clear()
        self.ui.qtTXTPrecio.clear()
        self.ui.qtTXTBodega.clear()
        self.ui.qtSPNSpinCantidad.setValue(0)

    def qtBTNAgregarArticulo(self):
        db = DB('C:\\Users\\aalva\\Progra\\Clone Proyecto final\\ProyectoFinal\\BaseDeDatos')
        if  self.ui.qtTXTNombre.text() =="" or self.ui.qtTXTPrecio.text() == "" or self.ui.qtTXTBodega.text() == "":
            QtWidgets.QMessageBox.warning(self, "Error", "Los campos no pueden estar vacíos")
        else:
            Nombre = self.ui.qtTXTNombre.text()
            Precio = self.ui.qtTXTPrecio.text()
            Cantidad = self.ui.qtSPNSpinCantidad.value()
            Informacion = [self.contador,Nombre, Precio, Cantidad]
            Bodega = self.ui.qtTXTBodega.text()
            db.insert(Bodega, Informacion)
            self.contador +=1
            print("El articulo se agrego correctamente")
            self.qtBTNLimpiar_clicked()
        


class GestionBodegas(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_qtWDWControlDeBodegas()
        self.ui.setupUi(self)

        self.ui.qtBTNLimpiar.clicked.connect(self.qtBTNLimpiar_clicked)

    def qtBTNLimpiar_clicked(self):
        # self.ui.qtCMBEmisor_2.currentIndex(0)
        # self.ui.qtCMBReceptor.currentIndex(0)
        # self.ui.qtCMBArticulos.currentIndex(0)
        # No hay opciones en los dropdown entonces aún no se pueden implementar esas líneas
        self.ui.qtSPNCantidadDeArticulos.setValue(0)