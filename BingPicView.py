# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(768, 660)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Bing.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.grid_main = QtWidgets.QGridLayout()
        self.grid_main.setObjectName("grid_main")
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setText("")
        self.image_label.setScaledContents(False)
        self.image_label.setObjectName("image_label")
        self.grid_main.addWidget(self.image_label, 0, 0, 1, 1)
        self.images_table = QtWidgets.QTableWidget(Form)
        self.images_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.images_table.setTabKeyNavigation(False)
        self.images_table.setProperty("showDropIndicator", False)
        self.images_table.setDragDropOverwriteMode(False)
        self.images_table.setShowGrid(True)
        self.images_table.setCornerButtonEnabled(True)
        self.images_table.setRowCount(10)
        self.images_table.setColumnCount(2)
        self.images_table.setObjectName("images_table")
        self.images_table.horizontalHeader().setVisible(False)
        self.images_table.horizontalHeader().setCascadingSectionResizes(False)
        self.images_table.horizontalHeader().setDefaultSectionSize(650)
        self.images_table.horizontalHeader().setHighlightSections(False)
        self.images_table.verticalHeader().setVisible(True)
        self.images_table.verticalHeader().setDefaultSectionSize(30)
        self.images_table.verticalHeader().setHighlightSections(False)
        self.grid_main.addWidget(self.images_table, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.grid_main, 0, 0, 1, 1)
        self.grid_buttons = QtWidgets.QGridLayout()
        self.grid_buttons.setObjectName("grid_buttons")
        self.apply_btn = QtWidgets.QPushButton(Form)
        self.apply_btn.setObjectName("apply_btn")
        self.grid_buttons.addWidget(self.apply_btn, 0, 1, 1, 1)
        self.confirm_btn = QtWidgets.QPushButton(Form)
        self.confirm_btn.setObjectName("confirm_btn")
        self.grid_buttons.addWidget(self.confirm_btn, 0, 2, 1, 1)
        self.update_btn = QtWidgets.QPushButton(Form)
        self.update_btn.setObjectName("update_btn")
        self.grid_buttons.addWidget(self.update_btn, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.grid_buttons, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Bing每日壁纸 via Tony"))
        self.apply_btn.setText(_translate("Form", "Apply"))
        self.confirm_btn.setText(_translate("Form", "Confirm"))
        self.update_btn.setText(_translate("Form", "Update"))

