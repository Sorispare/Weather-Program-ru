# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pogoda2.0.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pogoda(object):
    def setupUi(self, Pogoda):
        Pogoda.setObjectName("Pogoda")
        Pogoda.resize(2053, 769)
        Pogoda.setMinimumSize(QtCore.QSize(1316, 769))
        Pogoda.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        Pogoda.setFont(font)
        Pogoda.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        Pogoda.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Pogoda.setWindowIcon(icon)
        Pogoda.setWhatsThis("Погода")
        Pogoda.setStyleSheet("background-color: #28eb76;\n"
"border: none;\n"
"")
        self.MIN = QtWidgets.QLabel(Pogoda)
        self.MIN.setGeometry(QtCore.QRect(30, 110, 2001, 181))
        self.MIN.setMinimumSize(QtCore.QSize(1121, 181))
        self.MIN.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.MIN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MIN.setStyleSheet("color: white;\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.MIN.setObjectName("MIN")
        self.MAX = QtWidgets.QLabel(Pogoda)
        self.MAX.setGeometry(QtCore.QRect(30, 320, 1971, 171))
        self.MAX.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MAX.setStyleSheet("color: white;\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.MAX.setObjectName("MAX")
        self.TEXT = QtWidgets.QLabel(Pogoda)
        self.TEXT.setGeometry(QtCore.QRect(30, 540, 1991, 161))
        self.TEXT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TEXT.setStyleSheet("color: white;\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"")
        self.TEXT.setObjectName("TEXT")
        self.pushButton = QtWidgets.QPushButton(Pogoda)
        self.pushButton.setGeometry(QtCore.QRect(-40, -23, 2111, 81))
        self.pushButton.setMinimumSize(QtCore.QSize(1371, 81))
        self.pushButton.setMaximumSize(QtCore.QSize(999999, 999999))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
"        \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Pogoda)
        QtCore.QMetaObject.connectSlotsByName(Pogoda)

    def retranslateUi(self, Pogoda):
        _translate = QtCore.QCoreApplication.translate
        Pogoda.setWindowTitle(_translate("Pogoda", "Погода"))
        self.MIN.setText(_translate("Pogoda", "TextLabel"))
        self.MAX.setText(_translate("Pogoda", "TextLabel"))
        self.TEXT.setText(_translate("Pogoda", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pogoda = QtWidgets.QDialog()
    ui = Ui_Pogoda()
    ui.setupUi(Pogoda)
    Pogoda.show()
    sys.exit(app.exec_())
