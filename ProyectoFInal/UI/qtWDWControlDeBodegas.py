# Form implementation generated from reading ui file 'qtWDWControlDeBodegas.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_qtWDWControlDeBodegas(object):
    def setupUi(self, qtWDWControlDeBodegas):
        qtWDWControlDeBodegas.setObjectName("qtWDWControlDeBodegas")
        qtWDWControlDeBodegas.resize(819, 300)
        self.label = QtWidgets.QLabel(parent=qtWDWControlDeBodegas)
        self.label.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.label.setObjectName("label")
        self.qtCMBEmisor_2 = QtWidgets.QComboBox(parent=qtWDWControlDeBodegas)
        self.qtCMBEmisor_2.setGeometry(QtCore.QRect(80, 10, 161, 22))
        self.qtCMBEmisor_2.setObjectName("qtCMBEmisor_2")
        self.label_2 = QtWidgets.QLabel(parent=qtWDWControlDeBodegas)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 47, 13))
        self.label_2.setObjectName("label_2")
        self.qtCMBReceptor = QtWidgets.QComboBox(parent=qtWDWControlDeBodegas)
        self.qtCMBReceptor.setGeometry(QtCore.QRect(80, 50, 161, 22))
        self.qtCMBReceptor.setObjectName("qtCMBReceptor")
        self.qtCMBArticulos = QtWidgets.QComboBox(parent=qtWDWControlDeBodegas)
        self.qtCMBArticulos.setGeometry(QtCore.QRect(80, 90, 161, 22))
        self.qtCMBArticulos.setObjectName("qtCMBArticulos")
        self.label_3 = QtWidgets.QLabel(parent=qtWDWControlDeBodegas)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=qtWDWControlDeBodegas)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 47, 13))
        self.label_4.setObjectName("label_4")
        self.qtSPNCantidadDeArticulos = QtWidgets.QSpinBox(parent=qtWDWControlDeBodegas)
        self.qtSPNCantidadDeArticulos.setGeometry(QtCore.QRect(80, 130, 42, 22))
        self.qtSPNCantidadDeArticulos.setObjectName("qtSPNCantidadDeArticulos")
        self.qtTXEControlDeCambios = QtWidgets.QTextEdit(parent=qtWDWControlDeBodegas)
        self.qtTXEControlDeCambios.setGeometry(QtCore.QRect(300, 30, 501, 261))
        self.qtTXEControlDeCambios.setObjectName("qtTXEControlDeCambios")
        self.qtBTNEnviar = QtWidgets.QPushButton(parent=qtWDWControlDeBodegas)
        self.qtBTNEnviar.setGeometry(QtCore.QRect(20, 190, 101, 23))
        self.qtBTNEnviar.setObjectName("qtBTNEnviar")
        self.qtBTNLimpiar = QtWidgets.QPushButton(parent=qtWDWControlDeBodegas)
        self.qtBTNLimpiar.setGeometry(QtCore.QRect(160, 190, 101, 23))
        self.qtBTNLimpiar.setObjectName("qtBTNLimpiar")
        self.label_5 = QtWidgets.QLabel(parent=qtWDWControlDeBodegas)
        self.label_5.setGeometry(QtCore.QRect(300, 10, 47, 13))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(qtWDWControlDeBodegas)
        QtCore.QMetaObject.connectSlotsByName(qtWDWControlDeBodegas)

    def retranslateUi(self, qtWDWControlDeBodegas):
        _translate = QtCore.QCoreApplication.translate
        qtWDWControlDeBodegas.setWindowTitle(_translate("qtWDWControlDeBodegas", "CDP || Control De Bogedas"))
        self.label.setText(_translate("qtWDWControlDeBodegas", "Emisor"))
        self.label_2.setText(_translate("qtWDWControlDeBodegas", "Receptor"))
        self.label_3.setText(_translate("qtWDWControlDeBodegas", "Articulo"))
        self.label_4.setText(_translate("qtWDWControlDeBodegas", "Articulo"))
        self.qtBTNEnviar.setText(_translate("qtWDWControlDeBodegas", "Enviar"))
        self.qtBTNLimpiar.setText(_translate("qtWDWControlDeBodegas", "Limpiar"))
        self.label_5.setText(_translate("qtWDWControlDeBodegas", "Cambios"))
