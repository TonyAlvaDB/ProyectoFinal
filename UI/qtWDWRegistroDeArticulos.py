# Form implementation generated from reading ui file 'qtWDWRegistroDeArticulos.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_qtWDWRegistroDeArticulos(object):
    def setupUi(self, qtWDWRegistroDeArticulos):
        qtWDWRegistroDeArticulos.setObjectName("qtWDWRegistroDeArticulos")
        qtWDWRegistroDeArticulos.resize(414, 317)
        qtWDWRegistroDeArticulos.setStyleSheet("")
        self.layoutWidget = QtWidgets.QWidget(parent=qtWDWRegistroDeArticulos)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 811, 731))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=self.layoutWidget)
        self.frame.setStyleSheet("QFrame{\n"
"background-color:rgb(53, 53, 79);\n"
"}\n"
"\n"
"QPushButton{\n"
"font:87 12pt \"Arial Black\";\n"
"background-color:#000000ff;\n"
"color:rgb(20, 200, 220);\n"
"border-radius:5px;\n"
"border:1px solid white;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:black;\n"
"}\n"
"\n"
"QLabel{\n"
"font:87 12pt \"Arial Black\";\n"
"background-color:#000000ff;\n"
"color:rgb(20, 200, 220);\n"
"border-radius:5px;\n"
"border:1px solid white;\n"
"}\n"
"\n"
"QSpinBox{\n"
"font:87 12pt \"Arial Black\";\n"
"background-color:#000000ff;\n"
"color:rgb(20, 200, 220);\n"
"border-radius:5px;\n"
"border:1px solid white;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(20, 30, 151, 31))
        self.label.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.label.setStyleSheet("background:black")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 151, 25))
        self.label_2.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.label_2.setStyleSheet("background:black")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 151, 31))
        self.label_3.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.label_3.setStyleSheet("background:black")
        self.label_3.setObjectName("label_3")
        self.qtBTNAgregarArticulo = QtWidgets.QPushButton(parent=self.frame)
        self.qtBTNAgregarArticulo.setGeometry(QtCore.QRect(60, 220, 166, 25))
        self.qtBTNAgregarArticulo.setStyleSheet("background:black")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/shopping-cart (2).svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.qtBTNAgregarArticulo.setIcon(icon)
        self.qtBTNAgregarArticulo.setIconSize(QtCore.QSize(15, 15))
        self.qtBTNAgregarArticulo.setObjectName("qtBTNAgregarArticulo")
        self.qtTXTNombre = QtWidgets.QLineEdit(parent=self.frame)
        self.qtTXTNombre.setGeometry(QtCore.QRect(180, 30, 166, 20))
        self.qtTXTNombre.setObjectName("qtTXTNombre")
        self.qtBTNLimpiar = QtWidgets.QPushButton(parent=self.frame)
        self.qtBTNLimpiar.setGeometry(QtCore.QRect(250, 220, 88, 25))
        self.qtBTNLimpiar.setStyleSheet("background:black")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Downloads/book.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.qtBTNLimpiar.setIcon(icon1)
        self.qtBTNLimpiar.setObjectName("qtBTNLimpiar")
        self.qtSPNSpinCantidad = QtWidgets.QSpinBox(parent=self.frame)
        self.qtSPNSpinCantidad.setGeometry(QtCore.QRect(180, 120, 121, 31))
        self.qtSPNSpinCantidad.setStyleSheet("color:rgb(20, 200, 220);\n"
"background:black")
        self.qtSPNSpinCantidad.setObjectName("qtSPNSpinCantidad")
        self.qtTXTPrecio = QtWidgets.QLineEdit(parent=self.frame)
        self.qtTXTPrecio.setGeometry(QtCore.QRect(180, 80, 133, 21))
        self.qtTXTPrecio.setObjectName("qtTXTPrecio")
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 151, 31))
        self.label_4.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.label_4.setStyleSheet("background:black")
        self.label_4.setObjectName("label_4")
        self.qtTXTBodega = QtWidgets.QLineEdit(parent=self.frame)
        self.qtTXTBodega.setGeometry(QtCore.QRect(180, 170, 171, 22))
        self.qtTXTBodega.setObjectName("qtTXTBodega")
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(qtWDWRegistroDeArticulos)
        QtCore.QMetaObject.connectSlotsByName(qtWDWRegistroDeArticulos)

    def retranslateUi(self, qtWDWRegistroDeArticulos):
        _translate = QtCore.QCoreApplication.translate
        qtWDWRegistroDeArticulos.setWindowTitle(_translate("qtWDWRegistroDeArticulos", "CDP || Registro De Articulos"))
        self.label.setText(_translate("qtWDWRegistroDeArticulos", "Nombre:"))
        self.label_2.setText(_translate("qtWDWRegistroDeArticulos", "Precio:"))
        self.label_3.setText(_translate("qtWDWRegistroDeArticulos", "Cantidad:"))
        self.qtBTNAgregarArticulo.setText(_translate("qtWDWRegistroDeArticulos", "Agregar Articulo"))
        self.qtBTNLimpiar.setText(_translate("qtWDWRegistroDeArticulos", "Limpiar"))
        self.label_4.setText(_translate("qtWDWRegistroDeArticulos", "Bodega:"))
