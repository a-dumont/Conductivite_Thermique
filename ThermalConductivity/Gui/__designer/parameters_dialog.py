# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parameters_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Parameters(object):
    def setupUi(self, Dialog_Parameters):
        Dialog_Parameters.setObjectName("Dialog_Parameters")
        Dialog_Parameters.resize(400, 300)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog_Parameters)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Dialog_Parameters)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog_Parameters)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog_Parameters)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog_Parameters)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_width = QtWidgets.QLineEdit(Dialog_Parameters)
        self.lineEdit_width.setObjectName("lineEdit_width")
        self.gridLayout.addWidget(self.lineEdit_width, 0, 1, 1, 1)
        self.lineEdit_thickness = QtWidgets.QLineEdit(Dialog_Parameters)
        self.lineEdit_thickness.setObjectName("lineEdit_thickness")
        self.gridLayout.addWidget(self.lineEdit_thickness, 1, 1, 1, 1)
        self.lineEdit_length = QtWidgets.QLineEdit(Dialog_Parameters)
        self.lineEdit_length.setObjectName("lineEdit_length")
        self.gridLayout.addWidget(self.lineEdit_length, 2, 1, 1, 1)
        self.comboBox_sign = QtWidgets.QComboBox(Dialog_Parameters)
        self.comboBox_sign.setObjectName("comboBox_sign")
        self.comboBox_sign.addItem("")
        self.comboBox_sign.addItem("")
        self.gridLayout.addWidget(self.comboBox_sign, 3, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_Parameters)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog_Parameters)
        self.buttonBox.accepted.connect(Dialog_Parameters.accept)
        self.buttonBox.rejected.connect(Dialog_Parameters.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Parameters)

    def retranslateUi(self, Dialog_Parameters):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Parameters.setWindowTitle(_translate("Dialog_Parameters", "Sample Parameters"))
        self.label_2.setText(_translate("Dialog_Parameters", "Thickness: "))
        self.label.setText(_translate("Dialog_Parameters", "Width: "))
        self.label_3.setText(_translate("Dialog_Parameters", "Length: "))
        self.label_4.setText(_translate("Dialog_Parameters", "Sign: "))
        self.comboBox_sign.setItemText(0, _translate("Dialog_Parameters", "Positive"))
        self.comboBox_sign.setItemText(1, _translate("Dialog_Parameters", "Negative"))
