import os
import traceback
from  PyQt6 import QtCore,QtGui,QtWidgets
from UI.qtMainWindow import Ui_qtMainWindow
from UI.qtWDWAgregarBodega import Ui_qtWDWAgregarBodega
from UI.qtWDWControlDeBodegas import Ui_qtWDWControlDeBodegas
from UI.qtWDWInventarios import Ui_qtWDWInventarios
from UI.qtWDWRegistroDeArticulos import Ui_qtWDWRegistroDeArticulos
from Application.Core.moduloCore import *
from DataBase.DataBaseLogic import FileManager as DB
from PyQt6.QtWidgets import QTableWidgetItem

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
        db = DB('BaseDeDatos')
        if self.ui.qtTXTNombreDeBodega.text() == "":
            QtWidgets.QMessageBox.warning(self, "Error", "Los campos no pueden estar vacíos")
        else:
            nombreTabla = self.ui.qtTXTNombreDeBodega.text()
            columnas = ['nombre', 'precio', 'cantidad']
            db.create_table(nombreTabla, columnas)
            self.ui.qtTXTNombreDeBodega.clear()
            

class ModificarInventarios(QtWidgets.QDialog):
    def __init__(self) -> None:
        db = DB('BaseDeDatos')
        super().__init__()
        self.ui = Ui_qtWDWInventarios()
        self.ui.setupUi(self)
        for x in db.get_table_names():
            self.ui.comboBox.addItem(x)
        self.ui.comboBox.currentTextChanged.connect(self.get_information_on_table)
        

    def get_information_on_table(self, text):
        db = DB('BaseDeDatos')
        bodega = text
        listaBodega = db.get_full_list(bodega)
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)
        for i in range(db.count_rows_in_table(text)):
            row_position = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row_position)
            nombre = QTableWidgetItem(listaBodega[i][0])
            precio = QTableWidgetItem(str(listaBodega[i][1]))
            cantidad = QTableWidgetItem(str(listaBodega[i][2]))
            self.ui.tableWidget.setItem(row_position, 0, nombre)
            self.ui.tableWidget.setItem(row_position, 1, precio)
            self.ui.tableWidget.setItem(row_position, 2, cantidad)
        

class RegistroArticulos(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        db = DB('BaseDeDatos')
        self.ui = Ui_qtWDWRegistroDeArticulos()
        self.ui.setupUi(self)
        
        self.contador = db.count_rows_in_table("CDP")

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
        db = DB('BaseDeDatos')
        if  self.ui.qtTXTNombre.text() =="" or self.ui.qtTXTPrecio.text() == "" or self.ui.qtTXTBodega.text() == "":
            QtWidgets.QMessageBox.warning(self, "Error", "Los campos no pueden estar vacíos")
        else:
            Nombre = self.ui.qtTXTNombre.text()
            Precio = self.ui.qtTXTPrecio.text()
            Cantidad = self.ui.qtSPNSpinCantidad.value()
            Informacion1 = [Nombre, Precio, Cantidad]
            Informacion2 = [Nombre, Precio, 1]
            Bodega = self.ui.qtTXTBodega.text()
            for x in db.get_table_names():
                if x == "CDP":
                    db.insert(Bodega, Informacion1)
                else:
                    db.insert(x, Informacion2)
            QtWidgets.QMessageBox.information(self, "Confirmación", "El producto ha sido añadido exitosamente")
            self.qtBTNLimpiar_clicked()
            self.ui.qtTXTBodega.setText("CDP")
        

class GestionBodegas(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_qtWDWControlDeBodegas()
        self.ui.setupUi(self)
        db = DB('BaseDeDatos')

        for x in db.get_table_names():
            self.ui.qtCMBReceptor.addItem(x)
            self.ui.qtCMBEmisor_2.addItem(x)
            
        self.ui.qtCMBEmisor_2.setCurrentIndex(1)
        self.ui.qtCMBReceptor.setCurrentIndex(0)

        for x in db.get_just_names():
            self.ui.qtCMBArticulos.addItem(x)

        self.ui.qtBTNLimpiar.clicked.connect(self.qtBTNLimpiar_clicked)
        self.ui.qtBTNEnviar.clicked.connect(self.qtBTNEnviar_clicked)

    def qtBTNLimpiar_clicked(self):
        self.ui.qtSPNCantidadDeArticulos.setValue(0)

    def qtBTNEnviar_clicked(self):
        db = DB('BaseDeDatos')

        try:
            archivo = open(os.path.join("Reporte.txt"), 'a')

            emisor = self.ui.qtCMBEmisor_2.currentText()
            receptor = self.ui.qtCMBReceptor.currentText()
            articulos = self.ui.qtCMBArticulos.currentText()
            cantidad = self.ui.qtSPNCantidadDeArticulos.value()
            
            db.transfer_item(emisor, receptor, articulos, cantidad)
            
            archivo.write("----------------" + '\n')
            archivo.write("Emisor: "+ emisor + '\n')
            archivo.write("Receptor: "+ receptor + '\n')
            archivo.write("Articulos: "+ articulos + '\n')
            archivo.write("Cantidad enviada: "+ str(cantidad) + '\n')
            archivo.write("----------------" + '\n')
            archivo.close()

        except OSError as oE:
            archivo.close()
            QtWidgets.QMessageBox.warning(self, "Error", oE.strerror)
            print(oE.strerror)
        except BaseException:
            QtWidgets.QMessageBox.warning(self, "Error", traceback.format_exc())
            print(traceback.format_exc())
            archivo.close()
    
        