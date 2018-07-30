# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_About.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_about_dialog(object):
    def setupUi(self, about_dialog):
        about_dialog.setObjectName("about_dialog")
        about_dialog.resize(450, 340)
        self.gridLayout = QtWidgets.QGridLayout(about_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(about_dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(about_dialog)
        QtCore.QMetaObject.connectSlotsByName(about_dialog)

    def retranslateUi(self, about_dialog):
        _translate = QtCore.QCoreApplication.translate
        about_dialog.setWindowTitle(_translate("about_dialog", "About"))
        self.label.setText(_translate("about_dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">A Basic Fuel Car Simulator</span></p><p><br/></p><p><span style=\" font-size:10pt; font-weight:600;\">Author: </span><span style=\" font-size:10pt;\">Equinox</span></p><p><span style=\" font-size:10pt; font-weight:600;\">Year: </span><span style=\" font-size:10pt;\">2018</span></p><p><br/></p><p align=\"justify\"><span style=\" font-size:10pt;\">No licence or restrictions apply on this program. </span></p><p align=\"justify\"><span style=\" font-size:10pt;\">Made by using </span><span style=\" font-size:10pt; font-weight:600;\">Python, PyQt </span><span style=\" font-size:10pt;\">and </span><span style=\" font-size:10pt; font-weight:600;\">Qt Designer</span><span style=\" font-size:10pt;\">.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    about_dialog = QtWidgets.QDialog()
    ui = Ui_about_dialog()
    ui.setupUi(about_dialog)
    about_dialog.show()
    sys.exit(app.exec_())

