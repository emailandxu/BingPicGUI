# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(768, 660)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Bing.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout_2 = QtGui.QGridLayout(Form)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.grid_main = QtGui.QGridLayout()
        self.grid_main.setObjectName(_fromUtf8("grid_main"))
        self.image_label = QtGui.QLabel(Form)
        self.image_label.setText(_fromUtf8(""))
        self.image_label.setScaledContents(False)
        self.image_label.setObjectName(_fromUtf8("image_label"))
        self.grid_main.addWidget(self.image_label, 0, 0, 1, 1)
        self.images_table = QtGui.QTableWidget(Form)
        self.images_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.images_table.setTabKeyNavigation(False)
        self.images_table.setProperty("showDropIndicator", False)
        self.images_table.setDragDropOverwriteMode(False)
        self.images_table.setShowGrid(True)
        self.images_table.setCornerButtonEnabled(True)
        self.images_table.setRowCount(10)
        self.images_table.setColumnCount(2)
        self.images_table.setObjectName(_fromUtf8("images_table"))
        self.images_table.horizontalHeader().setVisible(False)
        self.images_table.horizontalHeader().setCascadingSectionResizes(False)
        self.images_table.horizontalHeader().setDefaultSectionSize(650)
        self.images_table.horizontalHeader().setHighlightSections(False)
        self.images_table.verticalHeader().setVisible(True)
        self.images_table.verticalHeader().setDefaultSectionSize(30)
        self.images_table.verticalHeader().setHighlightSections(False)
        self.grid_main.addWidget(self.images_table, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.grid_main, 0, 0, 1, 1)
        self.grid_buttons = QtGui.QGridLayout()
        self.grid_buttons.setObjectName(_fromUtf8("grid_buttons"))
        self.apply_btn = QtGui.QPushButton(Form)
        self.apply_btn.setObjectName(_fromUtf8("apply_btn"))
        self.grid_buttons.addWidget(self.apply_btn, 0, 1, 1, 1)
        self.confirm_btn = QtGui.QPushButton(Form)
        self.confirm_btn.setObjectName(_fromUtf8("confirm_btn"))
        self.grid_buttons.addWidget(self.confirm_btn, 0, 2, 1, 1)
        self.update_btn = QtGui.QPushButton(Form)
        self.update_btn.setObjectName(_fromUtf8("update_btn"))
        self.grid_buttons.addWidget(self.update_btn, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.grid_buttons, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Bing每日壁纸 via Tony", None))
        self.apply_btn.setText(_translate("Form", "Apply", None))
        self.confirm_btn.setText(_translate("Form", "Confirm", None))
        self.update_btn.setText(_translate("Form", "Update", None))

